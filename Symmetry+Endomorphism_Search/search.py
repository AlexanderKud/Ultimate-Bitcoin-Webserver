import secp256k1
import p2tr_util
from datetime import datetime

#---LCG Stuff---------------------------------------------------------------------#
lcg_m = 57896044618658097711785492504343953926418782139537452191302581570759080747168
lcg_a = 3618502788666131106986593281521497120401173883721090761956411348172442546699
lcg_c = # lcg_c value goes here

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

points = []
privkeys = []

while True:
    
    lcg_seed = (lcg_seed * lcg_a + lcg_c) % lcg_m;
    P = secp256k1.scalar_multiplication(lcg_seed)
    
    points.append(P)
    points.append(secp256k1.point_endo1(P))
    points.append(secp256k1.point_endo2(P))
    
    privkeys.append(lcg_seed)
    privkeys.append(secp256k1.priv_endo1(lcg_seed))
    privkeys.append(secp256k1.priv_endo2(lcg_seed))
    
    Q = secp256k1.negate_point(P)
    privKey = secp256k1.N - lcg_seed
    
    points.append(Q)
    points.append(secp256k1.point_endo1(Q))
    points.append(secp256k1.point_endo2(Q))
    
    privkeys.append(privKey)
    privkeys.append(secp256k1.priv_endo1(privKey))
    privkeys.append(secp256k1.priv_endo2(privKey))
    
    for i in range(len(points)):
        
        bitAddr = secp256k1.publickey_to_address(0, False, points[i])
        bitAddr_C = secp256k1.publickey_to_address(0, True, points[i])
        addrP2sh = secp256k1.publickey_to_address(1, True, points[i])
        addrbech32 = secp256k1.publickey_to_bech32_address(points[i])
        addrbech32_p2wsh = secp256k1.publickey_to_bech32_p2wsh_address(points[i])
    
        taproot_tweaked_public_key = p2tr_util.public_key_x_coordinate_to_taproot_tweaked_pubkey(points[i][1:33])
        bech32m_taproot_addr = p2tr_util.pubkey_to_segwit_v1_addr('bc', taproot_tweaked_public_key)
        
        if secp256k1.bloom_check(0, bitAddr):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {bitAddr} Private Key: {privkeys[i]} {secp256k1.privatekey_to_uwif(privkeys[i])}\n")
            print(f"Address: {bitAddr} Private Key: {privkeys[i]} {secp256k1.privatekey_to_uwif(privkeys[i])}")
                
        if secp256k1.bloom_check(0, bitAddr_C):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {bitAddr_C} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}\n")
            print(f"Address: {bitAddr_C} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}")
                
        if secp256k1.bloom_check(0, addrP2sh):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {addrP2sh} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}\n")
            print(f"Address: {addrP2sh} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}")
                
        if secp256k1.bloom_check(0, addrbech32):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {addrbech32} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}\n")
            print(f"Address: {addrbech32} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}")
                
        if secp256k1.bloom_check(0, addrbech32_p2wsh):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {addrbech32_p2wsh} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}\n")
            print(f"Address: {addrbech32_p2wsh} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}")
                
        if secp256k1.bloom_check(0, bech32m_taproot_addr):
            with open("found.txt", "a", encoding="utf-8") as f:
                f.write(f"Address: {bech32m_taproot_addr} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}\n")
            print(f"Address: {bech32m_taproot_addr} Private Key: {privkeys[i]} {secp256k1.privatekey_to_cwif(privkeys[i])}")
    
    save_counter += 1
    if save_counter == 100000:
        save_counter = 0
        with open("lcg_seed.txt", "w", encoding="utf-8") as f:
            f.write(f"{lcg_seed}\n")
        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Current LCG seed written to file')
    
    points.clear()
    privkeys.clear()
        
    
