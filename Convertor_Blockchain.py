# Convert All Private key to bitcoin address (p2pkh) and check just value balance from blockchain
# first install : pip install bit [Linux : pip3 install bit]
from bit import Key
import requests, json

# Convert Private key to Wallet Import Format (WI

# import all key from text file
filename = "PrivateKey_10M_Nov_2022.txt"
with open(filename, 'r', encoding='utf-8', errors='ignore') as fr:
    for Prikvatekey in fr.readlines():
        Privatekey = Prikvatekey.strip('\n').strip()

        Private_Key = Key.from_hex(Privatekey)
        # Create Address from Private Key
        addr = Private_Key.address
        req = requests.get("https://blockchain.info/balance?active=" + addr).json()
        balance = dict(req)[addr]['final_balance']
        print(addr, balance)