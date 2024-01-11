from web3 import Web3
import json
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
if web3.is_connected():
	print("Connection Successful")
else:
    print("Connection Failed")

deployed_contract_address = "0x5FC8d32690cc91D4c39d9d3abcBD16989F875707"
abi = 'artifacts/contracts/HelloWorld.sol/HelloWorld.json'

with open(abi) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

tx_hash = contract.functions.update('123').transact()
web3.eth.wait_for_transaction_receipt(tx_hash)
message = contract.functions.get().call()

print(message)