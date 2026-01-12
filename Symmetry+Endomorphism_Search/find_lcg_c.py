import random
import math

m = 57896044618658097711785492504343953926418782139537452191302581570759080747168
lcg_c = 1
#while True:
for _ in range(15):
    rnd = random.randrange(m)
    if math.gcd(rnd, m) == 1:
        lcg_c = rnd
        print(lcg_c)
        #break
    #lcg_c += 1
    #num -= 1
    #print(lcg_c)
