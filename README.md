# Ultimate-Bitcoin-Webserver
<b>Powered by <a href="https://github.com/AlexanderKud/Secp256k1_PythonLibrary">https://github.com/AlexanderKud/Secp256k1_PythonLibrary</a></b><br>

<pre>
  First thing create a bloomfilter from address txt file.
  You can download it from here <a href="http://addresses.loyce.club/">http://addresses.loyce.club/</a> right-hand column.
  Donwload and unpack to the folder with webserver. Or use your own txt address file.
  if you use your own  file with addresses uncomment and put its name in line 10 of create_bloomfilter.py
  After that just run create_bloomfilter.py
  In the browser: http://localhost:3333/1
  In the browser check the balance on the page: http://localhost:3333/0
</pre>
<pre>
  Paste in the Search Field:
  5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreCHK2Zzv - find the page by WIF
  from 1 up to 
  904625697166532776746648320380374280100293470930272690489102837043110636675 - go to the page #
  [1333] - change page increment
  (576460752303423489-1152921504606846977) - change random range
  @401738003616900500885184 - find the page by decimal private key
  $847e0d113ab3fc2f9e068785 - find the page by hex private key
</pre>
<pre>
  in the webserver.py lines 17-25 you can change the width of columns
  according to you screen.
  column1 = '490'
  column2 = '392'
  column3 = '266'
  column4 = '268'
  column5 = '270'
  column6 = '330'
  column7 = '480'
  column8 = '480'
  column9 = '398'
</pre>
<pre>
  in the webserver.py lines 28-29 you can change the speed of random and bruteforce.
  random_speed = 120
  bruteforce_speed = 120
  normal when it stops immediately after stop button clicked.
</pre>
<pre>
  in the webserver.py lines 31-33 you can change the mode. default is classic. random is commented.
  # classic or random (classic - secp256k1 G, random - random scalar and its pubkey as G)
  start_mode = 'classic' 
  #start_mode = 'random'
  that affects lines 39-49 in webserver.py:
  
  random mode picks a scalar from range 1...N and then it is used in scalar multiplication 
  and its public key as G (Generator Point).
  
  classic mode uses 1 and its public key as G (Generator Point).
  Or you can manually set for testing purposes any scalar from range 1...N
  to Point_Coefficient = ... and its public key will be used as G.
  
  if start_mode == 'classic':
    #Point_Coefficient = 55066263022277343669578718895168534326250603453777594175500187360389116729240
    #Point_Coefficient = 2
    Point_Coefficient = 1
    G = ice.scalar_multiplication(Point_Coefficient)
    current_mode = "classic_G_Point"
    
  if start_mode == 'random':
    Point_Coefficient = random.randrange(1, N)
    G = ice.scalar_multiplication(Point_Coefficient)
    current_mode = "random_G_Point"
</pre>
<pre>
    in the pop-up windows lower screenshots.
    private keys of additive inverse point and endomorphism are clickable and will lead to page where they are.
    sha256 hashes of Private and Public ECDSA Keys are all clickable and are used as private keys to lead to the page where the are.
</pre>
