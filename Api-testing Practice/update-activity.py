import requests

put_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/13"

header = {
    "Accept" : "application/json",
    "Content-Type" : "application/json"

}

request_payload = {
    "id": 13,
    "title": "Manika arjuna",
    "dueDate": "2025-06-04T11:14:20.119Z",
    "completed": True
}

response = requests.put(url=put_url,headers=header,json=request_payload)
print(response.json())
res_data = response.json()
assert response.status_code == 200
assert res_data["id"] == request_payload["id"]
assert res_data["title"] == request_payload["title"]