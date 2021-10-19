import requests
from termcolor import colored

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = input(colored("Enter Target Url: ","yellow"))
file = open("common.txt","r")
for line in file:
    word = line.strip()
    full_url = target_url + "/" + word
    response = request(full_url)

    if response:
        print(colored("Discovered Directory at this Link: ","green")+ colored(full_url,"magenta"))