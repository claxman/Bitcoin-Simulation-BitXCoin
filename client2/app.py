from flask import Flask, request, render_template
import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
import binascii
from collections import OrderedDict
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA


class Transaction:

    def __init__(self, sender_public_key, sender_private_key, recipient_public_key, amount):
        self.sender_public_key = sender_public_key
        self.sender_private_key = sender_private_key
        self.recipient_public_key = recipient_public_key
        self.amount = amount

    def to_dict(self):
        return OrderedDict({
            'sender_public_key': self.sender_public_key,
            'recipient_public_key': self.recipient_public_key,
            'amount': self.amount,
        })

    def sign_transaction(self):
        private_key = RSA.importKey(binascii.unhexlify(self.sender_private_key))
        signer = PKCS1_v1_5.new(private_key)
        hash = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(hash)).decode('ascii')


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/make/transaction')
def make_transaction():
    return render_template('make_transaction.html')

@app.route('/new/transaction')
def success_make_transaction():
    return render_template('success_transaction.html')

@app.route('/retryNew/transaction')
def failed_make_transaction():
    return render_template('failed_transaction.html')


@app.route('/view/transactions')
def view_transactions():
    return render_template('view_transactions.html')


@app.route('/wallet/new')
def new_wallet():
    random_gen = Crypto.Random.new().read
    
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.publickey()

    private_key = binascii.hexlify(private_key.export_key(format('DER'))).decode('ascii')
    public_key = binascii.hexlify(public_key.export_key(format('DER'))).decode('ascii')

    return render_template('walletGenerated.html',public_key = public_key, private_key = private_key)

@app.route('/generate/transaction', methods=['POST'])
def generate_transaction():

    url = request.url_root

    sender_public_key = request.form['sender_public_key']
    sender_private_key = request.form['sender_private_key']
    recipient_public_key = request.form['recipient_public_key']
    amount = request.form['amount']
    blockUrl = request.form['blockUrl']

    transaction = Transaction(sender_public_key, sender_private_key, recipient_public_key, amount)

    transaction.to_dict()
    signature =  transaction.sign_transaction()

    return render_template('node_confirm_transaction.html',url = url, blockUrl=blockUrl, sender_private_key=sender_private_key, sender_public_key=sender_public_key, recipient_public_key=recipient_public_key, amount=amount, signature=signature)

if __name__ == '__main__':
    app.run()
