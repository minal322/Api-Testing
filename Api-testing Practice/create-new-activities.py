import requests

post_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
header = {
    "accept" : "application/json",
    "content-type" : "application/json"
}
request_payload = {
    "id": 124,
    "title": "testing-api",
    "dueDate": "2025-06-03T13:24:12.048Z",
    "completed": True
}
response = requests.post(url=post_url,headers=header,json=request_payload)

print(response.status_code)
print(response.json())

res_data = response.json()

assert response.status_code == 200
assert res_data["id"] == request_payload["id"]
assert res_data["title"] == request_payload["title"]
assert res_data["completed"]  == request_payload["completed"]
