from sett.settings import Infura_config_url


from web3 import Web3

web3 = Web3.HTTPProvider(Infura_config_url)
print(web3.isConnected())

# convert to hexadecimals
print(Web3.api)
print(Web3.clientVersion)
print(Web3.toHex(10))
print(Web3.toHex(4000))
lester = Web3.toHex(text="duke lester")

#to string
print(Web3.toText(hexstr=lester))
number = Web3.toInt(hexstr=lester)
print(number)
number_2 = Web3.toInt(hexstr="0x7f840cdd6660")
print(number_2)

#check the address

my_address = '0xd3CdA913deB6f67967B99D67CDFa1712C293601'
print(Web3.isAddress(my_address))

sumAddress = Web3.isChecksumAddress(my_address)
print(sumAddress, 'sum address')


def checkSum(address):
    return Web3.isChecksumAddress(address)

my_address = "0xd3CdA913deB6f67967B99D67aCDFa1712C293601"
print(checkSum(my_address))
print(checkSum(sumAddress))

