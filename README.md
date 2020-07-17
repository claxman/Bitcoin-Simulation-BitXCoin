# Bitcoin-Simulation-BitXCoin
A Bitcoin network and wallet simulator.

There are 2 clients
* Alice (client-1)
* Bob (client-2)

similarly, there are 2 nodes
* Node-1
* Node-2


### Follow below instructions to simulate the network.
* Access Support Page by clicking [here](https://bitxcoin.herokuapp.com/)
* Accessing the **network** and **wallet**
    * Access **Alice** by clicking [here](https://bitx-client1.herokuapp.com/)
    * Access **Bob** by clicking [here](https://bitx-client2.herokuapp.com/)
    * Access **Node-1** by clicking [here](https://bitx-node1.herokuapp.com/)
    * Access **Node-2** by clicking [here](https://bitx-node2.herokuapp.com/)
* We'll try sending some ***BitX Coins*** from **Alice** to **Bob**.
    * Click on ***Generate Wallet*** on both clients.
    * Note down somewhere
    * Click on ***Transact*** frorm **navbar**
    * fill the **sender** and **recipient** details
    * You can change the node address to either of
        * https://bitx-node1.herokuapp.com/ 
        * https://bitx-node2.herokuapp.com/
    * Confirm Transaction
* Go to the node address which you filled while transacting coins.
    * Click on reload button to fetch the transactions.
    * click on ***mine***
    * And the transaction willl get updated in the **blockchain**
    * Also you'll be awarded the some **coin/coins** because you mined a block
* Click on **Configure** on the **node** page
    * Enter another node here, for example:
        * If current node is **node-1** then enter the link of **node-2**
        * Vice Versa
    * Click on ***Add Node***
* You'll have to **configure** both **nodes** for each other
    * This will make sure every node has the same ledger or the majority wins.  

 
**Author**
------
#### Chaitanya Laxman
