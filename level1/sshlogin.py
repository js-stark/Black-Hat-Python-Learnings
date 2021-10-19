import pexpect

PROMPT = ['# ','>>> ','>','\$']

def send_command(child,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)


def connect(user,host,password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret ==0:
        print('ERROR CONNECTING......')
        return
    if ret ==1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
        if ret ==0:
            print('ERROR IN CONNECTING..')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child



def main():
    host = input('enter the host IP address')
    user = input('enter the username of machine')
    password = input('enter the password of machine')
    child = connect(user,host,password)
    send_command(child,'cat /etc/shadow | gerp root;ps')

main()