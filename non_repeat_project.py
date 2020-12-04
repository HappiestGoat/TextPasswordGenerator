import sys

NULLED_ASCII = 33
open('password.txt', 'w').close()

f = open('dw_about_it.dll', 'a')    #
s = open('seed.txt', 'r')           #only meant to keep randomizing data
f.write(s.read())                   #

f = open('dw_about_it.dll', 'rb')
password = open('password.txt', 'a+')
fail = 0

i = 1

rng_range = 127 - NULLED_ASCII      #int(sys.argv[3]) - int(sys.argv[2])

def main():
    pw_len = int(input("Enter password length: "))
    make_password(i, pw_len)
    password = open('password.txt', 'r')
    print("Fails: ",fail,"\nPassword:\n",password.read())

def make_password(i, pwlen):
    f = open('dw_about_it.dll', 'a')    #
    s = open('seed.txt', 'r')           #only meant to keep randomizing data
    f.write(s.read())                   #

    random_number = 0
    f = open('dw_about_it.dll', 'rb')
    for x in list(f.read()):
        random_number = (random_number + x) % rng_range
    random_number += NULLED_ASCII
    first_char = chr(random_number);
    try:
        password.write(first_char)
    except:
        fail += 1
        i -= 1
    f.close()
    byte_count = 0

    while i <= pwlen:
        f = open('dw_about_it.dll', 'rb')
        for x in list(f.read()):
            byte_count += 1
            random_number = (random_number + x) % rng_range
        random_number += NULLED_ASCII
        if first_char == chr(random_number):
            make_password(i, pwlen)
            return 0
        try:
            password.write(chr(random_number))
        except:
            fail += 1
            i -= 1
        f.close()
        i += 1
    password.close()
    
if __name__ == "__main__":
    main()
