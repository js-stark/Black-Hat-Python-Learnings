import hashlib
from termcolor import colored

hashvalue = input('Enter the MD5 hash value of Password: ')
wordlist = input("enter the path for passwords list to check: ")

def findmd5password(hashvalue,wordlist):
    with open(wordlist,'r') as file:
        passwords = file.readlines()
        for passwords in passwords:
            hashobj =hashlib.md5()
            hashobj.update(passwords.strip().encode())
            x=str(hashobj.hexdigest())
            if x==hashvalue:
                print(colored('password found:'+passwords.strip(),'green'))
                quit()
            else:
                print(colored('password not match: '+passwords.strip(),'magenta'))

findmd5password(hashvalue,wordlist)

