import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = raw_input("Enter Target Url: ")
file_name = raw_input("Enter File to use: ")

file = open(file_name,"r")
for line in file:
    word = line.strip()
    full_url = word + "." + target_url
    response = request(full_url)

    if response:
        print("Discovered Subdomains at this Link: "+ full_url)
