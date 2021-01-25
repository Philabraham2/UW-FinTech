# Blockchain Proof of Authority Development Chain

I work as a new developer for Zbank, an innovative bank that is interested in using Blockchain technology to better serve clients and help the bank. My first project is to set up a private testnetwork (testnet) with my team of developers to explore how we can integrate blockchain into the bank. 

I set up a testnet in order to provide a virtual workspace where no real money is involved so our team can experiment with many blockchain applications without any negative implications.

## Blockchain Setup Installation 

Before beginning you must make sure that you have downloaded MyCrypto as well as Puppeth, Geth and know which os you are running. Since I am using windows operating system I have to use git-bash to run my operations. 

## Initializing Proof of Authority 

Proof of Authority is a reputation based way of approving blocks in a blockchain. This incentivizes validators to act ethically since their reputation is at stake and they do not want to lose it. 

### Creating Nodes and Genesis Block
    1. Create directory for the Nodes

        mkdir node 1 node 2
    2. Create accounts for the the two nodes that will be used by the network

        ./geth --datadir node1 account new
        ./geth --datadir node2 account new

    3.Get and save the public addresses of the node's key
        Node 1 : 0x8fBAa44c8E199f2dd69b90C1B2a144c7d65d631f
        Node 2 : 0x8009C57Fd3d4A62FDf5FAcDfFebbB45614fE5418

    4. Run Puppeth and create a network 
        I created a network called Philcoin
    
    5. We then follow the next steps:
        - Type 2 to configure new genesis block
        - type 2 for proof of authority 
        - paste in our public addresses for the nodes
        - paste the same addresses again for the accounts that need to be prefunded
        - choose no for pre-funding in order to keep the genesis as clean as possible 
        - determine a chain ID ~ I used 325
        - Type 2 to manage existing genesis
        - Type 2 to export genesis configurations and then continue with the default. This will generate image 1 in the screenshot tab
        
    
## Starting the BlockChain 
    1. Initialize nodes
        -using geth, initialize each node with the new philcoin.json.
            ./geth --datadir node1 init networkname.json
            ./geth --datadir node2 init networkname.json
    2. Launch the nodes to begin the mining process 
        - ./geth --datadir node1 --unlock "SEALER_ONE_ADDRESS" --mine --rpc --allow-insecure-unlock
        - ./geth --datadir node2 --unlock "SEALER_TWO_ADDRESS" --mine --port 30304 --bootnodes "enode://SEALER_ONE_ENODE_ADDRESS@127.0.0.1:30303" --ipcdisable --allow-insecure-unlock (this will connect the two nodes. We use port 30304 to help run the node)
        - type in the private password for each node 

## Connect Network to MyCrypto 
For the nodes to connect, a new custom network must be created in MyCrpto.

    1. Select "Add Custom Node", then add the  information that was created in the genesis.

    2. choose Custom in the "Network" column. Use the Chain ID from Puppeth.

    3. Use http://127.0.0.1:8545 for the URL.

    4. Select "Change Network" and select the Custom Node.

    5. Import the keystore file from the node1/keystore directory into MyCrypto. This will import the private key. Use the password of node1.

    6. Send a transaction from the node1 account to the node2 account. Use the public address of node 2 to send transaction. The wallet can be seen in image 2 and the transaction in image 3. 
    
## Conclusion

What this step by step process does is from scratch create a testnet in which you can create, mine and transact your own tokens. Here we can manipulate and try to find faults and new ways to implement blockchain into our banking system. This virtual environment allows us to afford making mistakes and finding holes in our system. Thus allowing the bank to find the best way to serve clients and create a system that helps further use blockchain technologies.






