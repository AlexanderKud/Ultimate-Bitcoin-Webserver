import secp256k1
import p2tr_util
from datetime import datetime

G = secp256k1.scalar_multiplication(1)

#---LCG Stuff---------------------------------------------------------------------#
lcg_m = 904625697166532776746648320380374280100293470930272690489102837043110636675
lcg_a = 180925139433306555349329664076074856020058694186054538097820567408622127336
lcg_c = # put c value here

lcg_file = open("lcg_seed.txt", 'r')
lcg_seed = int((lcg_file.readline()).strip())
lcg_file.close()
#---LCG Stuff---------------------------------------------------------------------#

bloomfile = 'bloomfile_btc.bf'
print(f'[{datetime.now().strftime("%H:%M:%S")}] - Loading bloomfilter from {bloomfile}')
secp256k1.bloom_load(0, bloomfile)
print(f'[{datetime.now().strftime("%H:%M:%S")}] - Done')

save_counter = 0

print(f'[{datetime.now().strftime("%H:%M:%S")}] - Search in progress ...')

while True:
    
    lcg_seed = (lcg_seed * lcg_a + lcg_c) % lcg_m;
    #print(f'[{datetime.now().strftime("%H:%M:%S")}] - Page: {lcg_seed}')
    startPrivKey = (lcg_seed - 1) * 128 + 1
    pub = secp256k1.scalar_multiplication(startPrivKey)
    
    for i in range(128):
        
        starting_key_hex = hex(startPrivKey)[2:].zfill(64)
        privKey = secp256k1.privatekey_to_uwif(startPrivKey)
        privKey_C = secp256k1.privatekey_to_cwif(startPrivKey)
        
        bitAddr = secp256k1.publickey_to_address(0, False, pub)
        bitAddr_C = secp256k1.publickey_to_address(0, True, pub)
        addrP2sh = secp256k1.publickey_to_address(1, True, pub)
        addrbech32 = secp256k1.publickey_to_bech32_address(pub)
        addrbech32_p2wsh = secp256k1.publickey_to_bech32_p2wsh_address(pub)
    
        taproot_tweaked_public_key = p2tr_util.public_key_x_coordinate_to_taproot_tweaked_pubkey(pub[1:33])
        bech32m_taproot_addr = p2tr_util.pubkey_to_segwit_v1_addr('bc', taproot_tweaked_public_key)
        
        if secp256k1.bloom_check(0, bitAddr):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {bitAddr} Private Key: {starting_key_hex} {privKey} \n")
            print(f"Address: {bitAddr} Private Key: {starting_key_hex} {privKey}")
                
        if secp256k1.bloom_check(0, bitAddr_C):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {bitAddr_C} Private Key: {starting_key_hex} {privKey_C} \n")
            print(f"Address: {bitAddr_C} Private Key: {starting_key_hex} {privKey_C}")
                
        if secp256k1.bloom_check(0, addrP2sh):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {addrP2sh} Private Key: {starting_key_hex} {privKey_C} \n")
            print(f"Address: {addrP2sh} Private Key: {starting_key_hex} {privKey_C}")
                
        if secp256k1.bloom_check(0, addrbech32):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {addrbech32} Private Key: {starting_key_hex} {privKey_C} \n")
            print(f"Address: {addrbech32} Private Key: {starting_key_hex} {privKey_C}")
                
        if secp256k1.bloom_check(0, addrbech32_p2wsh):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {addrbech32_p2wsh} Private Key: {starting_key_hex} {privKey_C} \n")
            print(f"Address: {addrbech32_p2wsh} Private Key: {starting_key_hex} {privKey_C}")
                
        if secp256k1.bloom_check(0, bech32m_taproot_addr):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {bech32m_taproot_addr} Private Key: {starting_key_hex} {privKey_C} \n")
            print(f"Address: {bech32m_taproot_addr} Private Key: {starting_key_hex} {privKey_C}")

        startPrivKey += 1
        pub = secp256k1.add_points(pub, G)
    
    save_counter += 1
    if save_counter == 5000:
        save_counter = 0
        with open("lcg_seed.txt", "w", encoding="utf-8") as f:
            f.write(f"{lcg_seed}\n")
        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Current LCG seed written to file')
        
