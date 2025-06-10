#For paged results parameter "page" and "per_page" should be passed in url ex:
# GET /public/v2/users?page=1&per_page=20 (max 100 results per page)
import requests

get_url = "https://gorest.co.in/public/v2/users"

parameters = {
    "page" : 3,
    "per_page" : 1
}
response = requests.get(url=get_url,params=parameters)

print(response.json())

assert response.status_code == 200