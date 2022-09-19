from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0x4bf6f9bd2AaBD2177De375c8E1Eb5bB0a0C945d4f"
account_2 = "0x77aacE27078820e29a0f5984D357bc032844e567"
priv_key2 = "bb03390d081cf86f14d15d3b595e6aed17057f300ccb2203e1f7a3842d98575a"
print(web3.isConnected())

nonce = web3.eth.getTransactionCount(account_2)

tx = {
    'nonce': nonce,
    'to': account_1,
    'value': web3.toWei(1, 'ether'), 
    'gas': 21000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.sign_transaction(tx, priv_key2)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# print("Transaction Hash: ", web3.toHex(tx_hash))
# print("Block Numbers: ", web3.eth.block_number)

# i = 0

# length_blockchains = web3.eth.block_number

# while i<= length_blockchains:
#     block = web3.eth.get_block(i)
#     for tx_hash in block['transactions']:
#         tx = web3.eth.get_transaction(tx_hash)
#         tx_obj = {'addr-sender': tx['from'], 'addr_receiver': tx['to'], 'value': tx['value']}

#         print("Block Number: ", block['number'])
#         print(tx_obj)
#         print("Value: ", tx['value'])
#         print(web3.toHex(tx_hash))
#         print("Block Hash: ", web3.toHex(block['hash']))
#         print("Tx Hash: ", (block['transactions']))
#         print("Block Parent Hash: ", web3.toHex(block['parentHash']), "\n")
#         print(web3.eth.getBalance(account_1))

#     i += 1