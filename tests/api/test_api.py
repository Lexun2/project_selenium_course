import allure, requests, pytest
from faker import Faker


@allure.feature('API')
@allure.story('API posts')
@allure.title("Тест позитивный регистрации пользователя")
@allure.description("Используем метод POST, для простой регистрации пользователя")
@pytest.mark.user_registration
def test_api_quest_positive_registration(api_url):
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



@allure.feature('API')
@allure.story('API posts')
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
@allure.story('API posts')
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
@allure.story('API posts')
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