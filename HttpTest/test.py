import requests

url = "https://httpbin.org/get"
response = requests.get(url)

print(response.content)