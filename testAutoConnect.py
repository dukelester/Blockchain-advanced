#testing the automatic connection to to the infura platform
from web3.auto.infura import Web3

print(Web3(Web3.isConnected(), 'This is a success auto Connection!'))