import pytest
import random


from utils.apis import APIs

@pytest.fixture(scope="module")
def apis():
    return APIs()

def test_get_user_validation(apis):
    response = apis.get("users")
    #print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_posts_validation(apis,load_user_data):
    # user_data = {
    #     "title": "Test Post",
    #     "body": "This is a test post created using Python requests.",
    #     "userId": 102
    # }
    user_data = load_user_data["new_post"]
    random_id = random.randint(100, 500)
    user_data["userId"] = random_id
    response = apis.post("posts", user_data)
    #print(response.json())
    print(response.status_code)
    assert response.status_code in [200,201]

    get_response = apis.get(f"posts/100")
    assert get_response.status_code == 200
    print(get_response.text)


def test_update_posts_validation(apis):
    user_data = {
  "userId": 1,
  "id": 1,
  "title": "Harry potter 1",
  "body": "Harry Potter"
}
    response = apis.put(f"posts/{user_data["id"]}", user_data)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200

    get_response = apis.get(f"posts/{user_data["id"]}")
    assert get_response.status_code == 200
    # print(get_response.text)

def test_delete_posts_validation(apis):
    response = apis.delete(f"posts/1")
    #print(response.json())
    assert response.status_code == 200
