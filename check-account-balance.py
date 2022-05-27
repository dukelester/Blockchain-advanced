''''
To find the amount of ether owned by an account, 
use the get_balance() method. At the time of writing, the 
account with the most 
ether has a public address of 
0x742d35Cc6634C0532925a3b844Bc454e4438f44e.
to convert the balance to Ether use the web3.fromWei() method, pass in the balance amount and the ether unit.
or another denomination, like wei, gwei, tether, gether, nano, grand, micro, milli, etc.

To convert back to wei, you can use the inverse function, toWei(). Note that Python’s 
default floating point precision is insufficient for this use case,
so it’s necessary to cast the value to a Decimal if it isn’t already. 
'''

from  web3 import Web3
from sett.settings import Infura_config_url

from decimal import Decimal
web3 = Web3(Web3.HTTPProvider(Infura_config_url))

# print(web3.isConnected(), 'This is a success Connection!')
#check if the web3 is connected

if web3.isConnected():
    print(web3.isConnected(), 'This is a success Connection!')
    
    #check the balance now
    account_balance = web3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
    print('my Account balance is \t', account_balance, '\n') #balance in wei
    #convert the balance to ether
    account_balance_in_ether = web3.fromWei(account_balance, 'ether')
    print('Balance in Ether \t', account_balance_in_ether, '\n')
    
    balance_in_grand = web3.fromWei(account_balance, 'grand')
    print('Account balance in Grand \t', balance_in_grand, '\n')
    balance_in_nano = web3.fromWei(account_balance, 'nano')
    print('Account balance in Nano \t', balance_in_nano, '\n')
    balance_in_gether = web3.fromWei(account_balance,'gether')
    print('Account balance in Gether \t', balance_in_gether, '\n')
    balance_in_kether = web3.fromWei(account_balance,'kether')
    print('Account balance in Kether \t', balance_in_kether, '\n')
    balance_in_tether = web3.fromWei(account_balance,'tether')
    
    #connect back to wei using the toWei() method
    
    account_balance_from_kether_to_wei = web3.toWei(Decimal(balance_in_kether), 'wei')
    print('Back to wei from kether \t', account_balance_from_kether_to_wei, '\n')
    
    
else:
    print('failed to connect, Try again!', web3.isConnected())
    