import requests
import os

os.system('cls')

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("=" * 50)
print(response.text)
print(type(response.text))
print("\n")
print(response.json())
print(type(response.json()))