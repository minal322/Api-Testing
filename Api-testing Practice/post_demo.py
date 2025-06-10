import requests
import os
import json
filepath = os.path.join(os.path.dirname(__file__),"..","data","users.json")
print(filepath)
base_url = "https://reqres.in/"

header = {
    "Content-Type" : "application/json",
    "x-api-key": "reqres-free-v1"
}

# req_payload= {
#     "name": "Minal",
#     "job": "SDET"
#
# }
file_obj = open(filepath,"r")

json_payload = json.load(file_obj)

user_data = {
    "name": "Minal",
    "job": "SDET"
    }
response = requests.post(url=base_url+"/api/users",headers=header,data=json.dumps(user_data))
res_data = response.json()
print(response.text)
assert response.status_code == 201