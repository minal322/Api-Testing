import requests

post_url = "https://gorest.co.in/public/v2/users"
token = "Bearer 778e9ff0a93b49ff12da1353a67677a1e9fb1551d6e65409b1a5cdc5455cc384"
header = {
    "Content-Type" : "application/json",
    "Authorization" : token
}
req_body = {
"id": 123459,
  "name": "abc",
  "email": "a1234569@gmail.com",
  "gender": "female",
  "status": "active"
}

response = requests.post(url=post_url,headers=header,json=req_body)
print(response.json())

res_data = response.json()

assert res_data["name"] == req_body["name"]
assert response.status_code == 201


getresponse = requests.get(url=post_url+"/"+str(res_data["id"]) , headers=header)

print(getresponse.json())

assert getresponse.status_code == 200