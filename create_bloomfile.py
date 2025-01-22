import secp256k1
from datetime import datetime
import os

files = os.listdir(os.getcwd())
for f in files:
    if 'Bitcoin_addresses' in f:
        filename = f

_elem = 53000000*2
_fp = 0.000001
_bits, _hashes = secp256k1.bloom_para(_elem, _fp)
_bf = (b'\x00') * (_bits//8)

print(f'[{datetime.now().strftime("%H:%M:%S")}] Creating Bloomfilter from {filename}')
counter = 0
with open(filename) as in_file:
    for item in in_file:
        secp256k1.add_to_bloom(item.strip(), _bits, _hashes, _bf)
        counter +=1
print(f'[{datetime.now().strftime("%H:%M:%S")}] Bloomfilter ready: {counter} elements')

f = open("count.txt", "w")
f.write(f"{counter}\n")
f.write(f"{datetime.today().strftime("%d.%m.%Y")}\n")
f.close()

bloomfile = 'bloomfile_btc.bf'
print(f'[{datetime.now().strftime("%H:%M:%S")}] Writing Bloomfilter to {bloomfile}')
secp256k1.dump_bloom_file(bloomfile, _bits, _hashes, _bf, _fp, _elem)
print(f'[{datetime.now().strftime("%H:%M:%S")}] Bloomfilter written')
print(f'[{datetime.now().strftime("%H:%M:%S")}] Done. Press <ENTER> to exit...')
input()
