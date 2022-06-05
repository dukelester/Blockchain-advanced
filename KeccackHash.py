from sett.settings import Infura_config_url
from web3 import Web3

connect = Web3(Web3.HTTPProvider(Infura_config_url))
print(connect, 'connected')

#a function for doing a  keccak hashing

def KeccakHashing(data):
    return Web3.keccak(text=data)

hashed_data = KeccakHashing('hello duke lester')
print(hashed_data)
