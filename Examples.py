#get the account balances uisning the balanceOf method
from web3 import Web3
from sett.settings import Infura_config_url

web3 = Web3(Web3.HTTPProvider(Infura_config_url))

print(web3.isConnected(), 'connection success')

balance = web3.eth.balanceOf('0xe5900F903098D059Bf9605fEb95303F657f1A82A')
print(balance)