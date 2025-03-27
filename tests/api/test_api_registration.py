#Тестовое задание для Ваним Стрибука


# import allure, requests




# @allure.feature('API')
# @allure.story('API posts')
# @allure.title("Тест получения всех постов")
# @allure.description("Используем метод GET, хотим получить список всех постов неавторизованным пользователем")
# def test_api_quest_get_all_posts(api_url):
#     response = requests.get(f"{api_url}/posts", timeout=5)
#     assert response.status_code == 200, f"Запрос API (GET /posts/ не работает, код {response.status_code}"



# @allure.feature('API')
# @allure.story('API posts')
# @allure.title("Тест создать пост")
# @allure.description("Используем метод POST для создания поста")
# def test_api_quest_add_post(api_url, api_headers):
#     post = {
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1,
#     }
#     response = requests.post(f"{api_url}/posts", json=post, headers=api_headers)
#     assert response.status_code == 201, f"Запрос API (POST /posts/ не работает, код {response.status_code}"
#     assert "id" in response.json(), "В ответе нет поля id"
#     assert response.json()["userId"]==1, "id поста не совпадает в ответе с отправленным"



# @allure.feature('API')
# @allure.story('API posts')
# @allure.title("Тест удалить пост")
# @allure.description("Используем метод DELETE для удаления поста")
# def test_api_quest_delete_post(api_url):
#     response = requests.delete(f"{api_url}/posts/1")
#     assert response.status_code == 200, f"Запрос API (DELETE /posts/1 не работает, код {response.status_code}"
#     # assert requests.get(f"{api_url}/posts/1", timeout=5).status_code == 404, "Пост не удалился, он найден"