import requests
import json
class ReqResAPIs:
    base_url = "https://reqres.in/"
    def __init__(self):
        self.header = {
            "Content-Type" : "application/json",
            "x-api-key": "reqres-free-v1"

        }

    def get(self,endpoint):
        get_url = self.base_url+endpoint
        response = requests.get(url = get_url, headers=self.header)
        return response


    def post(self,endpoint,data):
        post_url = self.base_url+endpoint
        response = requests.get(url = post_url, headers=self.header,data=json.dumps(data))
        return response
