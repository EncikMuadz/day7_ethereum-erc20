### Summary
- The smart contract, the web3.py interface(JSON-RPC)

### Disclaimer
Smart contract based on: 
- https://hashnode.com/post/how-to-build-your-own-ethereum-based-erc20-token-and-launch-an-ico-in-next-20-minutes-cjbcpwzec01c93awtbij90uzn

### Development
- get and modify the code `DONE`
- User access
    - metamask as wallet
- Blockchain
    - Ropsten network and ganache
- Smart Contract
    - compile contract using Remix IDE, deploy compiled contract to testnet `TBD`
    - verify contract before deploying ABI to the mainnet `TBD`

### Deployment
- buy token `TBD`
- launch ICO page `TBD`

### API
- web3.py(JSON-RPC) -> FastAPI

### Microservices
- Client
    - create env
    - update packages - `pip install -U pip setuptools wheel`
    - Update docs
    - django users, graphql
- Blob storage
    - IPFS node
    - Interface using IPFS API
- Brownie templating
    - Automated smart contract creation
    - Automated smart contract deployment
    - graphql
- Reverse proxy
    - Nginx
    - traefik
- Blockchain node
    - DapsNodeIo for production
    - ganache/hardhat for development
    - geth for development/production
- Chainlink Node:
    - Middleware between blockchain and external data
    - geth

### TO DO
- Investigate using openstack implementation
- quantum ledger from openstack implementation