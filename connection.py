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

