from fastapi import FastAPI

from web3 import Web3

ganache_url = "http://ganache:8545"

webthree = Web3(Web3.HTTPProvider(ganache_url))

app = FastAPI(title='API for Web3 JSON RPC')

@app.get('/api/connection/status/')
async def is_connected():
    return { 'data' : webthree.isConnected() }

@app.get('/api/eth/block/number/')
async def block_number():
    return { 'data' : webthree.eth.blockNumber }

@app.get('/api/eth/accounts/')
async def known_accounts():
    return { 'data' : webthree.eth.accounts }

@app.get('/api/eth/accounts/{account}')
async def account_balance(account: str):
    return { 'data' : webthree.eth.get_balance(account) }