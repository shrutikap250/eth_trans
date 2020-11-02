from web3 import Web3

infura_url = "https://ropsten.infura.io/v3/8e82bf4be272449db8be55799ac649a2"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

acc1 = "0x03ef0a6911AcFAd46Bc8324D356f8682aC479E13"

acc2 = "0xc34757Caa1c3AbF696538423B73bD516D51f64f6"

acc1_bal = web3.eth.getBalance(acc1)
acc1_eth = web3.fromWei(acc1_bal, "ether")
print("Acc1 balance before:")
print(acc1_eth)

acc2_bal = web3.eth.getBalance(acc2)
acc2_eth = web3.fromWei(acc2_bal, "ether")
print("Acc2 balance before: ")
print(acc2_eth)

p_key = "1b75ea4c0bf525a82756318f0fde5231d81cf9028123205230609c54c67d9f8e"

nance = web3.eth.getTransactionCount(acc1)

tx = {
	'nonce': nance,
	'to': acc2,
	'value': web3.toWei(1,"ether"),
	'gas': 200000,
	'gasPrice': web3.toWei('50', 'gwei')
}

singed_tx = web3.eth.account.signTransaction(tx, p_key)
tx_hash = web3.eth.sendRawTransaction(singed_tx.rawTransaction)
print(web3.toHex(tx_hash))

receipt = web3.eth.waitForTransactionReceipt(tx_hash)
#time.sleep(90)

acc1_bal = web3.eth.getBalance(acc1)
acc1_eth = web3.fromWei(acc1_bal, "ether")
print("Acc1 balance After: ")
print(acc1_eth)

acc2_bal = web3.eth.getBalance(acc2)
acc2_eth = web3.fromWei(acc2_bal, "ether")
print("Acc2 balance After: ")
print(acc2_eth)
