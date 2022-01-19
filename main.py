import json
from web3 import Web3
import requests

# Example transaction 
# https://polygonscan.com/tx/0x1e85ace98f4fc4ad7b1b64465df81d0a275d494421e553e23a238b156f42b17f

try:
    ALCHEMY_KEY = "Rt4_MeHNZEE8mQWVi9Ct-uSppHNSDmOG"
except:
    print("Please insert your Alchemy API Key!")

w3 = Web3(Web3.HTTPProvider("https://polygon-mainnet.g.alchemy.com/v2/"+ALCHEMY_KEY))

# includes the standard ERC20 ABI info
ERC20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501

# configures web3 to point towards the USDT token address
# make sure that these addresses are Ethereum-checksummed! (use this tool: https://ethsum.netlify.app/ to make sure)
USDT_ADDRESS = '0xc2132D05D31c914a87C6611C10748AEb04B58e8F'
FROM_ADDRESS = '0x5350E1068f0E138ff306990B16fA4910d970c692'
TO_ADDRESS = '0x9d2b758E3ffd2569c6956676fAE7f8B71A53Ffb5'

from_Block = '0x16C5376'
to_Block = '0x16C537A'

usdt = w3.eth.contract(address=USDT_ADDRESS, abi=ERC20_ABI)

transfer_json = requests.post('https://polygon-mainnet.g.alchemy.com/v2/'+ALCHEMY_KEY, json={"jsonrpc": "2.0","id": 0,"method": "alchemy_getAssetTransfers","params": [{"fromBlock": from_Block,"toBlock": to_Block,"fromAddress": FROM_ADDRESS,"toAddress": TO_ADDRESS,"contractAddresses": [USDT_ADDRESS],"category": ["erc20"]}]})
json_response = transfer_json.json()
#print(json_response)

transfer_val = (json_response['result']['transfers'][0]['rawContract']['value'])

# convert hexadecimal make to decimal format 
val = (int(transfer_val, 16))

print("USDT TRANSFERED:")
print("--> FROM: " + FROM_ADDRESS)
print("--> TO: " + TO_ADDRESS)

# unit conversion!
print(val/1000000)

