### Summary
- The smart contract, the web3.py interface(JSON-RPC)

### Disclaimer
Smart contract based on: 
- https://hashnode.com/post/how-to-build-your-own-ethereum-based-erc20-token-and-launch-an-ico-in-next-20-minutes-cjbcpwzec01c93awtbij90uzn

### Development
- get and modify the code `DONE`
- metamask as wallet
- Ropsten network and ganache for development
- compile contract using Remix IDE, deploy compiled contract to testnet `TBD`
- verify contract before deploying ABI to the mainnet `TBD`
- buy token `TBD`
- launch ICO page `TBD`

### API
- web3.py(JSON-RPC) -> FastAPI

### Microservices
- Client
    - create env
    - update packages - `pip install -U pip setuptools wheel`
    - Update docs
- Blob storage
    - IPFS node
    - Interface using IPFS API
- Brownie templating
- Reverse proxy
- Blockchain node
    - DapsNodeIo for production
    - ganache/hardhat for development
- Chainlink Node:
    - Middleware between blockchain and external data
    - geth