import random
import math

m = 904625697166532776746648320380374280100293470930272690489102837043110636675
lcg_c = 0
num = m // 3
#while True:
for _ in range(10):
    rnd = random.randrange(m)
    if math.gcd(rnd, m) == 1:
        lcg_c = rnd
        print(lcg_c)
        #break
    #num -= 1
    #print(lcg_c)
