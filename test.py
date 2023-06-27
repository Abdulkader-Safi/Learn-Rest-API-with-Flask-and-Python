import requests

BASE = "http://127.0.0.1:5000/"

name = "Abdulkader Safi"
response = requests.get(BASE + "helloworld/" + name)
print("Get")
print(response.json())
