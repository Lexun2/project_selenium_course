import allure, requests, pytest
from faker import Faker
from requests.auth import HTTPBasicAuth # для авторизации Basic (логин:пароль)
from base64 import b64encode
from unittest.mock import patch, Mock


@allure.feature('API')
@allure.story('API Login')
@allure.title("Тест позитивный регистрации пользователя")
@allure.description("Используем метод POST, для простой регистрации пользователя")
@pytest.mark.user_registration
def test_api_quest_positive_registration_and_auth(api_url):
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
    payload_data_auth = {
        "email": payload_data["email"],
        "password": payload_data["password"]
    }
    response = requests.post(f"{api_url}/jwt/create/", json = payload_data)
    assert response.status_code==200, "Ошибка получения JWT токена"
    token = response.json()["access"]
    print("\n"+token+"\n")



@allure.feature('API')
@allure.story('API Login')
@allure.title("Тест негативный регистрации пользователя без какого либо поля json")
@allure.description("Используем метод POST, для негативной регистрации пользователя без 1го поля")
@pytest.mark.user_registration
@pytest.mark.parametrize("key",["username", "email", "password"])
def test_api_quest_negative_registration_and_auth(api_url, key):
    faker = Faker("ru_RU")
    payload_data = {
                    "username": faker.name(),
                    "email": faker.email(),
                    "password": faker.password(8)
                    }
    del payload_data[key]
    response = requests.post(f"{api_url}/users/", payload_data)
    assert response.status_code==400, "Ошибка создания пользователя"





@allure.feature('API')
@allure.story('API Login')
@allure.title("Тест регистрации пользователя с username = 1 символ")
@allure.description("Используем метод POST, для регистрации пользователя с username 1 символ")
@pytest.mark.user_registration
def test_api_quest_positive_registration_1_symbol_username(api_url):
    faker = Faker("ru_RU")
    payload_data = {
                    "username": faker.pystr(max_chars = 1),
                    "email": faker.email(),
                    "password": faker.password(8)
                    }
    response = requests.post(f"{api_url}/users/", payload_data)
    print(response.json())
    print(response.status_code)
    assert response.status_code==201, "Ошибка создания пользователя"
    assert response.json()["username"]==payload_data["username"] , "Username don't equal"
    assert response.json()["email"]==payload_data["email"] , "Username don't equal"


@allure.feature('API')
@allure.story('API Login')
@allure.title("Тест регистрации пользователя с username = 255 символ")
@allure.description("Используем метод POST, для регистрации пользователя с username 255 символ")
@pytest.mark.user_registration
def test_api_quest_positive_registration_255_symbol_username(api_url):
    faker = Faker("ru_RU")
    payload_data = {
                    "username": faker.pystr(max_chars = 1)*255,
                    "email": faker.email(),
                    "password": faker.password(8)
                    }
    response = requests.post(f"{api_url}/users/", payload_data)
    print(response.json())
    print(response.status_code)
    assert response.status_code==201, "Ошибка создания пользователя"
    assert response.json()["username"]==payload_data["username"] , "Username don't equal"
    assert response.json()["email"]==payload_data["email"] , "Username don't equal"



@allure.feature('API')
@allure.story('API Login')
@allure.title("Тест регистрации пользователя с username = 256 символ")
@allure.description("Используем метод POST, для регистрации пользователя с username 256 символ")
@pytest.mark.user_registration
def test_api_quest_positive_registration_255_symbol_username(api_url):
    faker = Faker("ru_RU")
    payload_data = {
                    "username": faker.pystr(max_chars = 1)*256,
                    "email": faker.email(),
                    "password": faker.password(8)
                    }
    response = requests.post(f"{api_url}/users/", payload_data)
    print(response.json())
    print(response.status_code)
    assert response.status_code==400, "Почему то удалось создать пользователя c username 256 символов"
    assert response.json()["username"][0] == "Ensure this field has no more than 255 characters.", "Ожидаем другую ошибку"


@allure.feature('API')
@allure.story('API Login')
@allure.title("Тест позитивный удаления пользователя")
@allure.description("Используем метод DELETE, для позитивного удаления пользователя")
@pytest.mark.user_registration
@pytest.mark.use_mock #(reason="feature not work")
@patch('test_api.requests.delete')
@patch('test_api.requests.get')
def test_delete_user(mock_get, mock_delete, api_url, auth_headers):
    mock_delete.return_value = Mock(status_code=204)
    mock_get.return_value = Mock(status_code=401)
    response = requests.delete(f"{api_url}/users/me/", headers=auth_headers)
    assert response.status_code == 204 #тут 400 ждем 204
    # получить данные удаленного пользователя
    me_response = requests.get(f"{api_url}/users/me/", headers=auth_headers)
    # проверка, что пользователь удален и токен больше не действителен
    assert me_response.status_code == 401


@allure.feature('API')
@allure.story('API Login')
@allure.title("Тест позитивный изменения пароля пользователя")
@allure.description("Используем метод POST, для позитивного изменения пароля пользователя")
@pytest.mark.user_registration
def test_user_password_change(api_url, auth_headers, registered_user):
    faker = Faker("ru_RU")
    payload_data = {
                    "new_password": faker.password(10),
                    "current_password": registered_user["password"]
                        }
    response = requests.post(f"{api_url}/users/set_password/", headers=auth_headers, json=payload_data)
    assert response.status_code == 200, "При изменении пароля пользователя вернулся не ожидаемый код ответа"