import sys
import math
NULLED_ASCII = 33

open('password.txt', 'w').close()

f = open('dw_about_it.dll', 'a')	#only meant to keep randomizing data
s = open('seed.txt', 'r')		#
f.write(str(s))				#

f = open('dw_about_it.dll', 'rb')
password = open('password.txt', 'a+')
random_number = 0
fail = 0
bit_count = 0;
i = 1
writes = int(input("Enter password length: "))
rng_range = 127 - NULLED_ASCII #int(sys.argv[3]) - int(sys.argv[2])
while i <= writes:
    f = open('dw_about_it.dll', 'rb')
    for x in list(f.read()):
        bit_count += 1
        random_number = (random_number + x) % rng_range
    random_number += NULLED_ASCII #int(sys.argv[2])
    try:
        password.write(chr(random_number))
    except:
        fail += 1
        i -= 1
    f.close()
    bit_count = 0
    i += 1
password.close()

password = open('password.txt', 'r')
print("Fails: ",fail,"\nPassword:\n",password.read())
