import requests
import os

os.system('cls')

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

response_dic = response.json()

for key, value in response_dic.items():
    print(f"key => {key} | value => {value}")