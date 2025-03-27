import pytest, requests
from faker import Faker

# Для тестового задания Вани Стрибука
# @pytest.fixture
# def base_url():
#     return "https://jsonplaceholder.typicode.com"

# @pytest.fixture
# def api_url(base_url):
#     return base_url+""



@pytest.fixture
def base_url():
    return "http://95.182.122.183"


@pytest.fixture
def api_url(base_url):
    return base_url+":8000/api/v1"

@pytest.fixture
def api_headers():
    return { 'Content-type': 'application/json; charset=UTF-8',  }



@pytest.fixture
def registered_user(api_url):
    faker = Faker("ru_RU")
    payload_data = {
                    "username": faker.name(),
                    "email": faker.email(),
                    "password": faker.password(8)
                    }
    response = requests.post(f"{api_url}/users/", payload_data)
    # print(response.json())
    # print(response.status_code)
    assert response.status_code==201, "Ошибка создания пользователя"
    assert "id" in response.json(), "В ответе нет id"
    assert response.json()["username"]==payload_data["username"] , "Username don't equal"
    assert response.json()["email"]==payload_data["email"] , "Username don't equal"
    return payload_data


@pytest.fixture
def auth_token(api_url, registered_user):
    auth_data = {
        "email": registered_user["email"],
        "password": registered_user["password"],
    }
    response = requests.post(f"{api_url}/jwt/create", json = auth_data)
    assert response.status_code == 200
    return response.json()["access"]


@pytest.fixture
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}