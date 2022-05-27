#here we will try to find info about blocks

from web3 import Web3
from sett.settings import Infura_config_url

#connect to Infura node

web3 = Web3(Web3.HTTPProvider(Infura_config_url))
#latest block
latest_block = web3.eth.getBlock('latest')
print(latest_block, 'Latest Block \n')
#block by number using the blockNumber attribute
block_number = web3.eth.blockNumber
print(block_number, 'BLOCK NUMBER \n')

#get the block details for the block given its number
block_details = web3.eth.get_block(block_number)
print(block_details, 'HERE block details\n\n')

#get a block using the hash

get_block_using_hash = web3.eth.get_block('0xe220b240d42e0573d0ee24b364c7bac179c58a060f778e5e9041a66272dc6e56')
print(get_block_using_hash, 'Block using the hash, \n\n')

new_block = web3.eth.get_block(14853688)
print(new_block, 'The block from Etherscan \n\n')
