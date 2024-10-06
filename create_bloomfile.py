import secp256k1 as ice
from datetime import datetime
import os

files = os.listdir(os.getcwd())
for f in files:
    if 'Bitcoin_addresses' in f:
        filename = f

_bits, _hashes = ice.bloom_para(53000000*2, 0.000001)
_bf = (b'\x00') * (_bits//8)
time = datetime.now().strftime("%H:%M:%S")
print(f"[{time}] Creating Bloomfilter from {filename}")
counter = 0
with open(filename) as in_file:
    for item in in_file:
        ice.add_to_bloom(item.strip(), _bits, _hashes, _bf)
        counter +=1
time = datetime.now().strftime("%H:%M:%S")
print(f"[{time}] Bloomfilter ready: {counter} elements")
date_today = datetime.today().strftime("%d.%m.%Y")
f = open("count.txt", "w")
f.write(f"{counter}\n")
f.write(f"{date_today}\n")
f.close()

bloomfile = 'bloomfile_btc.bf'
time = datetime.now().strftime("%H:%M:%S")
print(f'[{time}] Writing Bloomfilter to {bloomfile}')
ice.dump_bloom_file(bloomfile, _bits, _hashes, _bf)
time = datetime.now().strftime("%H:%M:%S")
print(f"[{time}] Bloomfilter written")
time = datetime.now().strftime("%H:%M:%S")
print(f"[{time}] Done. Press <ENTER> to exit...")
input()
