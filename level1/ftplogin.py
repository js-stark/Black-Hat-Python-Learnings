import ftplib

def anonlogin(hostname):
    try:
        ftp=ftplib.FTP(hostname)
        ftp.login('msfadmin','msfadmin')
        print(hostname, "FTP Anonymus login succesful")
        ftp.quit()
        return True
    except Exception as e:
        print(f"{hostname} refused to connect as credential are wrong")

host = input('Enter the host ip address')
anonlogin(host)


