import requests

url = "http://localhost:5000/author_token"

res = requests.post(url=url, data={'grant_type':'password', 'username':'johnson', 'password':'123456'})
#res = requests.post(url=url, data={'grant_type':'password', 'username':'johnson1', 'password':'123456'})
#print(res.text)
print(res.text)
print(res.status_code)