import requests

url = "http://localhost:5000/author_token"

# 先取得 access_token
res_token = requests.post(url=url, data={'grant_type':'password', 'username':'johnson', 'password':'123456'})
# 取得 response 資料
res_data = res_token.json()

# 定義 request 的 header
param = {
    'Authorization':'Bearer ' + res_data.get('access_token'),
    'Accept':'application/json',
    'Content-Type':'application/json'
}

res2 = requests.get(url, headers=param)
print(res2.json())