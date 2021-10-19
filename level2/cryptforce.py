import crypt
from termcolor import colored

class Crptography:

    def __init__(self):
       
        with open('level2/crypt.txt','r') as file:
            for i in file.readlines():
                x=i.split(':')[1].strip()[:2]
                y=i.split(':')[1].strip()
                self.x=x
                self.y=y

                with open('level2/cryptdict.txt','r') as file:
                    for i in file.readlines():
                        password=i.split('\n')[0]
                        crypt_pass=crypt.crypt(password,self.x)
                        if crypt_pass==self.y:
                            print(colored("Password Found: "+password,'magenta'))
                        else:
                            pass
                
                 
    # def cryptdict(self):

    #     with open('level2/cryptdict.txt','r') as file:
    #         for i in file.readlines():
    #             m=i.split('\n')[0]
    #             crypt_pass=crypt.crypt(m,self.x)
    #             print(crypt_pass)


    
obj = Crptography()