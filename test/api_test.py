import requests

api_get = requests.get(url="http://localhost:5000/api/test")
print(api_get.json())

api_post = requests.post(url="http://localhost:5000/api/test")
print(api_post.json)

api_delete = requests.delete(url="http://localhost:5000/api/test")
print(api_delete.json())