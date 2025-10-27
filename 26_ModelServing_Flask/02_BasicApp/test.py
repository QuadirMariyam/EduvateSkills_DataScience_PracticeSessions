import requests


url = "http://127.0.0.1:5000/square"
data = {"number":100}

response=requests.post(url, json=data)
print(response.json())