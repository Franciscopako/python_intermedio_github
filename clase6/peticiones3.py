import requests
import os

os.system('cls')

response = requests.get("https://jsonplaceholder.typicode.com/users")

response_dic = response.json()

for data in response_dic:
    print(data)