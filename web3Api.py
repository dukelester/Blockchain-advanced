from logging import exception
from sett.settings import Infura_config_url
from web3 import Web3

url = "https://mainnet.infura.io/v3/16543f54f4384a4791e6289b79882e2b"
web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())


latest_block = web3.eth.get_block('latest')
print(latest_block, '\n\n\n')

"""
AttributeDict({'baseFeePerGas': 90444461788,
'difficulty': 15529979393711777,
'extraData': HexBytes('0x617369612d65617374322d6e776a6e'),
'gasLimit': 30029295, 
'gasUsed': 5056511, 
'hash': HexBytes('0x07e2f847c7a626e5ad4028d1cee35b1c1b4cd85aa68602c0f00657715c12b262'),
'logsBloom': HexBytes('0x080080c0014002054010800c1000801d50400104409502580018000804040206504235e80a008a4000005d02040201010a4016802861a0e08204045e1028a20402480022400820e8880040a880600318386100468504001808048000d00000440740020ca6084c80044000002cc018d52208825b020006064200041104082038000002a180200140088102404a8b080657010040030200200400204289110020420c41912182280c000160d210000840000020090220a08000260802300d00053810002202000024018800210840004948046248852a0080ad0002081a2a61088016680a50400110680410d4100003000888604021408500873a488202080201'),
'miner': '0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8',
'mixHash': HexBytes('0x1d446f760fe6e828150f22a46e920664a5bd8677a4575aa492b513ea7b88c128'),
'nonce': HexBytes('0x6a7b5e514b405c44'), 
'number': 14909928,
'parentHash': HexBytes('0xabcf575874e98fef7b3a60dd50a49be29b3455c8c4e8e53855cca401e1897c32'),
'receiptsRoot': HexBytes('0x8327e3d176df865c769bea2cbe3615f6e81d00e646d83c916df2a178bead5023'),
'sha3Uncles': HexBytes('0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'), 
'size': 40546, 
'stateRoot': HexBytes('0xaffd7c505ac3b59be46af94a5b333f79f9fc0537855c87f21654f520a0227f2b'), 
'timestamp': 1654443747, 
'totalDifficulty': 50915158324507306147228, 
'transactions': [HexBytes('0x122449631a9eb427c883f29e44807e726926f5d42d9909e579afeb448dda565a'),
HexBytes('0x74b71bf4f87c2a1aa39fe558cb6d3cf9739e281e7bdcfe98d3b64d499b12a780'),
HexBytes('0xd295e70acf17ef30fdee314ea05cbdcb80e1f4bce4d2f0bc2df98f3fe6c7888b'), 
HexBytes('0xba2dcf63e0515dff47682db0ec7f6d3b7091e904c2508b688c44b468f3197ac5'), 
HexBytes('0x9955e9a3692bc31bca89775078a19940fcb765c832dbf065693cf8386a6e4a12'),
HexBytes('0xe0bd144578b301d21f73f6af2668a48007c551e1ee85d47e47e016e7b560abc2'),
HexBytes('0xd3865cbee5f044e0e6e88490c3002921c86a642a58d4017c482288ac8d19b982'),
HexBytes('0x491508bf6997690c8a0ddad6cf48d205b320b45307f8953979581f9128c9ebb2'),
HexBytes('0x57b4097db195ba3fb7f26b2a7cd8fe885d8ca56426105b4768faf2df8c280379'),
HexBytes('0xa7521262d6f224e96c0bf62f47fdacbbb534f44d30a569cdd984192355f87671'),
HexBytes('0xeb2daf941fb384e5d70ce33f5be4690e586be29145aa5878e7a876d90962e40a'),
HexBytes('0x05b6d47aecc321551c5dbc2eeb0eef75c37a1886fc7177c060ab549936274ecb'),
HexBytes('0xa7bdd8589cc7a055e826f9e97d879e484490be6cf7959adb069c8263d41dbb64'),
HexBytes('0x4541293851e238d62878a06ddf453bdca9601e02af8c3706fb2f4ba0219a5ee1'),
HexBytes('0x78ef5c936545b93fe7779e33a22789a231db279dad9d6d82eefb2eaa120772f6'),
HexBytes('0x7b1d39620bc84527b9e99072c009da306ec529a3629de5bfb1a9e913818c39ff'),
HexBytes('0x66a2ee9c406fc2404f10191d6b1ab43d5cee0d7955fa3e0309c24d8e1265ce57'),
HexBytes('0xfd16806eee8328185aa36fa57555b0164310f7d8188a94d9f9a0a96b9e272308'),
HexBytes('0x006bbec0dbe9ebe3b9b1308548ee2f0ea8842ed3cf019a9546ae17f7b955c409'),
HexBytes('0x25a5a83f5f6667a1c6f54d13e694d7bda627fdfebdd2f19a9929cdc4503f60e5'),
HexBytes('0x105e726f73bfe633c96a61c3884f869c73d26891dcc2b0287174e37087b5e7c2'),
HexBytes('0xcc681f513fd4127df70ef935b2318e5261c41557fe1eb83b40d258ef546ba532'),
HexBytes('0x242bb76e42a7c269e188199033cddb9a1f3e163b98adc604c73c68fa1e7d861b'),
HexBytes('0x9d7b9137826c0b9aebc58c38532a07874f4166ee4f587380e77b4ce756a51354'),
HexBytes('0x966d884c65ff361d122dc3a72359b7f5c62a8cb53e3c12d7a787f14ac84150cb'),
HexBytes('0xe00ccf1c323a89eded63ba94dcca63fac53143091bc3352c9cb0bbc5ca532ef5'),
HexBytes('0xa974e6bd36a0e36e3b65269a8de77024599d1adcdf87cc5f25320f8d8f5730f9'),
HexBytes('0x750ba7ae8b0b02e0a06cc898c74d388574fa4be20f772f73d475cf6fc8f27dca'),
HexBytes('0x08cab38cdaf810daf4abc92d5cedc0a28e8717a251bd434a878abe67d67fc795'),
HexBytes('0x5ffdc7c98174e707a14e71d708f44e74a30a56b9e9aa95a2c8e28492ebac50af'),
HexBytes('0xa3da431ed7cbdd7526dbb1be57024e1e2042913567cb003bad6c95c457c9e519'),
HexBytes('0x29613773ee1f2a5ef3c46c8f57393d07a361a304975b0ac77ffa774a5e346138'),
HexBytes('0x4c345e3974afe9173e833de93a1870a153e18a0496423ad8e2e3efb1eb7b4813'),
HexBytes('0x208befa5bbcf9251ba840927593abf2ba80bcb1f903f49b2133be792af5ecfc8'),
HexBytes('0x688033429b2e7d682a9ac10b4010f03573fc5cc8f0c4afbd4f739a5d181c553c'),
HexBytes('0x2af33c6e93c86da28db98608c6b7eeab5cf5b68af3c38831a78f6aae624dffa9'),
HexBytes('0xa1c402f5a8a5ec8f5346927189ae4374a26f8af97d1c8afb51dc426f9c4ad2f9'),
HexBytes('0x756ad3eec42adf86fd8fafa7b93b7a4e36c2332f67333c4a56e8d281c47c0041'),
HexBytes('0xcfedc2b12064d4a865e6de7c0ee3c6adbe0ffd7d99d22d2695ecd5af89d7b1af'),
HexBytes('0x2078ed694480184c502e028d90753b48f6788eb73d799ae566a578e16ce956ec'),
HexBytes('0xe475c10e63b5c2ea6970ff31a0b14091cd1e7e29ed450caaa515bd93dea6a4f1'),
HexBytes('0x805fd88de9a8a9c9271550df23f9bf6883c1d238a2e3e0c5c937e4e3b0484965'),
HexBytes('0xa65100d038b089ece12529edaf78501983ce1cc1dded43a3832341c0f2330723'),
HexBytes('0x31c166e890e1b5a7b3c86af400a039c456767a8d74afaafc1a0d92d63eaee8a0'),
HexBytes('0xc1d757f0ca304d4024e45e9d920247f078af8eef5847a329c83987bae275284a'),
HexBytes('0xfde38647fc1c8d7e625d14f8604a240c78540bf3efcdca11479ee0e168e2f248'),
HexBytes('0xf670581ac79ea3394acf8c317041c8e57a86816fe86b587e299f5442474f22a3'),
HexBytes('0x8001a61ed3ed870cdc5b4d16d27f756e582e236681a0b90144efc9375daabc15'),
HexBytes('0x50f8d868dd61e0a5e4b4c51d3236e98207efe8e38e68861a16b988fe138ed574'),
HexBytes('0xcee6fcc71ec758c58dafc21a5e842099efd76e0e8ddbdad643723f93fa19bd0d'),
HexBytes('0x5ff2cb49a071289c8d46787c4025a227f47aca83ce0ec97eec2b9797cdbec06b'),
HexBytes('0x2502b5408fdc20f2f02fc8bd9483023ec3764c86d9aed3eeb6f1de847918ce5d'),
HexBytes('0x505e5e34d2972a199cabb2969d6323baefc2329e9b9be67dbf91bfbe6a5a6ddc'),
HexBytes('0x5534aaaf1284e28736b9509284805db5979e911363e5f87f0edee5dad00ac50c'),
HexBytes('0x4109b1594961aad9181bb9fa21f7936e4c5f8252297876441ecb70b570b89727'),
HexBytes('0xe5a21e39b40d804ba549d6152e45d917a0946421671e7bbef175a00a188052ae'),
HexBytes('0x097a8f3d219f06b871c7a7d8ca2ac77ee06e279267bff438e2235c4117d3aaa2'), 
HexBytes('0xb7b45643303974d6be2c8a590eb6d22bb1825d6345edbf65bac6846274a38045'),
HexBytes('0x9e24901e7f79ebee77edb85c1c79f5ba80c1b2e08a06fa08d1a73a1902c65bfd'),

HexBytes('0x5319225e318f6aee1706bfa4f90883f61db6d195b583cb1284d3f89cb60f32a8'),
HexBytes('0xc8eb97a21a91f509ca66466aae9887e22b59339488905525aa86ba992673aa38'),
HexBytes('0x03f3689398f59f451f532d99ba7cce3c901eabfaa57b1fb7460bed48c07ed2f5'), HexBytes('0x2579b0aac70e39724c65ade718653798b0e99245d988b52e29ca88f144fc6953'), HexBytes('0xce3928f47e9b61f6263c8d84164ad3b639c0d63b1aeec034ea6dd816675fcc25'), HexBytes('0x30b6c9a0a418801fef6ab90b72b5f60d29876a20808ca894ddcce01e4901178c'), HexBytes('0xb8cd51af2ab0b7bef52508c903b6b01e4b45cc728ebcc62e276682b8001a9d4d'), HexBytes('0x7d943460f35aa2f06cdc4b2927befa209c1c9f5336a9e25cf200d4743907828a'), HexBytes('0x63d4f20d8ceaaeaea5cc92ae0671c4ff532c46d5f28ae3592237b497e8dc775c'), HexBytes('0xba70d0ed3ae4a3f0875e51cb89e808e02ca5431e8374b8b680e566c75198973f'), HexBytes('0x3e562c763409081546f5738c3ca1cb9c5f755c53579c16b8e943e889146e92eb'), HexBytes('0x483fe2f1ef763191678c5cf34e9333f6d3e888363d369199d2fe47ec27f82d3d'), HexBytes('0x10c74f4f05b88162ff33e350653e2f38b874cdbbf5d9e7d845edafefeba3fdfe'), HexBytes('0xbf0545090ec80ae21b465d15e8139686e039ace9f926baf49c8315d4f79ca08c'), HexBytes('0x15613e71da2a4a5995c4b147085db76d5d4be32c5545b48478552152f8afcd69'), HexBytes('0x88b280a16dea46d4477fb39d8b35ba18d5314db0d9f0bf485ed6f1542ac6ab4b'), HexBytes('0x9b447347c7ea0e0d618fe53d9161f701b038f30bc022eefd82f2fae7c7008dff'), HexBytes('0x6587d366a32b3f869b4bdbba2a0f8219fb124fb95b2664ebabc2c42ecec6ba4f'), HexBytes('0xe984d4aee1147ec9496fafe196bfff968b4a11dffda4c0fa6030ae0e184a0cc5'), HexBytes('0xe5d311146ed8e14ca9bdd322df13c4dbbffa6a106f24e4ecc7eecf096f1bccb7'), HexBytes('0x4463f4d0278b4100069d5b5c2d59dc8fa497bc5c0a076f9cf7128f7eabbc7702')], 'transactionsRoot': HexBytes('0xb548cdf0140a13328c09b0b157537a7f25a067712c0f9d38873800f5c3414884'), 
'uncles': []})

"""

#the attributeDict behaves like a dictionaly .. so lets access all the elements and data in it
block_number = latest_block['number'] #just like a dictionary
print(block_number)
nonce = latest_block.nonce
print(nonce, 'nonce')

convert_nonce = Web3.toInt(nonce)
print("converted nonce to number is" , convert_nonce)
#convert to hexdecimals
nonce_to_hex = Web3.toHex(convert_nonce)
print('converted to hexadecimals  ', nonce_to_hex)


def getBlockDetails(block):
    block_number = block.number
    print('block number ', block_number)
    
    nonce = block.nonce
    #convert to number 
    nonce = Web3.toInt(nonce)
    print('block nonce is ', nonce)
    
    #difficulty
    difficulty = Web3.toInt(block.difficulty)
    print('block difficulty is ', difficulty)
    #gasLimit
    gasLimit = block.gasLimit
    print('gasLimit ', gasLimit)
    
    #gasUsed
    gasUsed = block.gasUsed
    print('gas used ', gasUsed)
    #hash 
    block_hash = block['hash']
    print('block hash ', block_hash)
    #parentHash
    parentHash = block['parentHash']
    print('parentHash ',parentHash)
    #miner
    miner = block['miner']
    print('miner ', miner)
    #logsBloom
    logsBloom = block['logsBloom']
    print('logsBloom ', logsBloom)
    #receiptsRoot
    receiptsRoot = block.receiptsRoot
    print('receiptsRoot ', receiptsRoot)
    #sha3Uncles 
    sha3Uncles = block.sha3Uncles
    print('sha3Uncles ', sha3Uncles)
    #block size 
    size = block['size']
    print('block size is ', size)
    #stateRoot
    stateRoot = block.stateRoot
    print('stateRoot ',stateRoot)
    #timestamp
    timestamp = block.timestamp
    print('timestamp ', timestamp)
    #totalDifficulty
    totalDifficulty = block.totalDifficulty
    print('totalDifficulty  ',totalDifficulty)
    #transactions 
    transactions = block.transactions
    print('transactions ', len(transactions))
    
getBlockDetails(latest_block)

#web3.eth.coinbase ==> get the coinbase 
mining = web3.eth.mining
print(mining)

#hashrate 
hashrate = web3.eth.hashrate
print('hashrate is ', hashrate)

#max_priority_fee
max_priority_fee = web3.eth.max_priority_fee
print('max_priority_fee  ', web3.toWei(max_priority_fee, 'gwei'))

#gas_price 
gas_price = web3.eth.gas_price
print('gas price ', web3.fromWei(gas_price, 'ether'))
accounts = web3.eth.accounts
print('accounts, ', accounts)
try:
    coinbase = web3.eth.coinbase
    print('coinbase ', coinbase)
    #mining
    mining = web3.eth.mining
    print(mining)
        
except:
    print('not found')
    
    
    
    