from sett.settings import Infura_config_url
from web3 import Web3

my_test = Web3(Web3.HTTPProvider(Infura_config_url))
print(my_test.isConnected(), 'Yaaay Connected!')