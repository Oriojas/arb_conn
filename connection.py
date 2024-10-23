import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open("artifacts/Saludo_metadata.json") as f:
    info_json = json.load(f)

ABI = info_json["output"]["abi"] # primer requisito para la conexion

CONTRACT = "0x28494B6d0a26923B5bdcE8c9a25F9A27C9c7Da93" # segundo requisito
WALLET = os.environ["WALLET"] # tercer requisito
PRIV_KEY = os.environ["PRIV_KEY"] # cuarto requisito

arbitrum_rpc = "https://endpoints.omniatech.io/v1/arbitrum/sepolia/public" #quinto requisito

w3 = Web3(Web3.HTTPProvider(arbitrum_rpc)) # establecemos la coneccion con el RPC

if w3.is_connected():
    print("-" * 50)
    print("Connected to Arbitrum RPC endpoint")
else:
    print("Connection Failed")

contract_address = CONTRACT
contract_abi = ABI

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

account_address = WALLET
private_key = PRIV_KEY

result = contract.functions.leerSaludo().call()

print("-" * 50)
print(f"Ultimo saludo: {result}")


function_data = contract.functions.guardarSaludo("Hola desde python recargado II").build_transaction({
    'from': account_address,
    'gas': 5000000,
    'gasPrice': w3.to_wei('10', 'gwei'),
    'nonce': w3.eth.get_transaction_count(WALLET),
    'chainId': 421614,
})

signed_transaction = w3.eth.account.sign_transaction(function_data, private_key)
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

print(f"HASH: {transaction_hash.hex()}")

result2 = contract.functions.leerSaludo().call()

print("-" * 50)
print(f"Ultimo saludo: {result2}")

