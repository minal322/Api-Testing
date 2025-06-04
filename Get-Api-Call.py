import requests
header = {
    "Accept" : "application/json"
}
response = requests.get(url="https://fakerestapi.azurewebsites.net/api/v1/Activities/4",headers=header)

print(response.status_code)
print(response.json())

assert response.status_code == 200

