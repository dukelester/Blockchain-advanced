from web3 import Web3
from sett.settings import Infura_config_url

#test the connection to the block
web3 = Web3(Web3.HTTPProvider(Infura_config_url))


if web3.isConnected():
    print('Yaaay Connected!', web3.isConnected())
    get_latest_block = web3.eth.get_block('latest')
    print(get_latest_block, 'lets see the latest block')
    #using the hash
    block_info = web3.eth.get_block('0x15f0eb1e5e037e8fb7ce09814f9e8f52c52ec9e3eb4a562cf31bfe025296443b')
    print(block_info, 'using the hash')
    balance = web3.eth.get_balance('0xcF95237Ce34d4B5bF1E7De4474EE1dcc01f24Ca9')
    print(balance, 'using the balance')
    convert_to_ether = web3.fromWei(balance, 'ether')
    print(convert_to_ether, 'converted to ether \n\n')
    

    '''
    There are a few options for making transactions:

        send_transaction()

        Use this method if:
        you want to send ether from one account to another.

        send_raw_transaction()

        Use this method if:
        you want to sign the transaction elsewhere, e.g., a hardware wallet.

        you want to broadcast a transaction through another provider, e.g., Infura.

        you have some other advanced use case that requires more flexibility.

        Contract Functions

        Use these methods if:
        you want to interact with a contract.
        Web3.py parses the contract ABI and makes those functions available via
        the functions property.

        construct_sign_and_send_raw_middleware()

        Use this middleware if:
        you want to automate signing when using w3.eth.send_transaction or ContractFunctions.
    '''
    
    
    'Looking up transactions :: You can look up transactions using the web3.eth.get_transaction function.'
    get_transaction = web3.eth.get_transaction('0x632a9abcc2f0e04226211285dc7bad0d6d0bb1566b70b2315b35ce43713b30fa')
    print(get_transaction, 'transaction details \n\n')
    
    '''
    Looking up receipts
Transaction receipts can be retrieved using the web3.eth.get_transaction_receipt API.
    '''
    transaction_receipt = web3.eth.get_transaction_receipt('0x632a9abcc2f0e04226211285dc7bad0d6d0bb1566b70b2315b35ce43713b30fa')
    print(transaction_receipt, 'transaction receipt \n\n')
else:
    print('An Error ocurred while connecting!', web3.isConnected())