import pytest
from utils.reqres_apis import ReqResAPIs

@pytest.fixture(scope="module")
def apis():
    return ReqResAPIs()

# def test_get_user_validation(apis):
#     response = apis.get("api/users?page=2")
#     #print(response.json())
#     assert response.status_code == 200
#     assert len(response.json()) > 0

def test_create_user_validation(apis):
    user_data = {
    "name": "assfdfdg",
    "job": "assasfd"
    }
    response = apis.post("api/users", user_data)
    print(response.status_code)
    #print(response.text)
    #assert response.status_code == 201
