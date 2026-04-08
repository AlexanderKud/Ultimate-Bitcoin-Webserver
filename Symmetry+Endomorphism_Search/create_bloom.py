import secp256k1
from datetime import datetime
import os

files = os.listdir(os.getcwd())
for f in files:
    if 'Bitcoin_addresses' in f:
        filename = f

_elem = 54000000*2
_fp = 0.000001
secp256k1.init_bloom(0, _elem, _fp)

print(f'[{datetime.now().strftime("%H:%M:%S")}] Creating Bloomfilter from {filename}')
counter = 0
with open(filename) as in_file:
    for item in in_file:
        secp256k1.bloom_add(0, item.strip())
        counter +=1
print(f'[{datetime.now().strftime("%H:%M:%S")}] Bloomfilter ready: {counter} elements')


bloomfile = 'bloomfile_btc.bf'
print(f'[{datetime.now().strftime("%H:%M:%S")}] Writing Bloomfilter to {bloomfile}')
secp256k1.bloom_save(0, bloomfile)
print(f'[{datetime.now().strftime("%H:%M:%S")}] Bloomfilter written')
