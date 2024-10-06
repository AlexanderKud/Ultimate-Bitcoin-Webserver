# Ultimate-Bitcoin-Webserver

![Screenshot from 2024-10-06 14-12-43](https://github.com/user-attachments/assets/f1902aee-e3e5-4029-b898-d2596fc201e1)

![Screenshot from 2024-10-06 14-13-08](https://github.com/user-attachments/assets/12c4e3eb-212e-4539-b3a6-9b9c3f45c307)

<pre>
  First thing create a bloomfilter from address txt file.
  You can download it from here <a href="http://addresses.loyce.club/">http://addresses.loyce.club/</a> right-hand column.
  Donwload and unpack to the folder with webserver. Or use your own txt address file.
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
