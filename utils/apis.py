import requests

class APIs:
    base_url = "https://jsonplaceholder.typicode.com/"
    def __init__(self):
        self.header = {
            "Content-Type" : "application/json"
        }

    def get(self,endpoint):
        get_url = self.base_url+endpoint
        response = requests.get(url = get_url, headers=self.header)
        return response


    def post(self,endpoint,data):
        post_url = self.base_url+endpoint
        response = requests.get(url = post_url, headers=self.header,json=data)
        return response

    def put(self,endpoint,data):
        post_url = self.base_url+endpoint
        response = requests.get(url = post_url, headers=self.header,json=data)
        return response

    def delete(self,endpoint):
        post_url = self.base_url+endpoint
        response = requests.get(url = post_url, headers=self.header)
        return response