import requests

# Инициализация сессии
session = requests.Session()

# 1. Делаете GET-запрос для получения страницы и CSRF токена
response = session.get("http://127.0.0.1:8000/company/register/")

# Проверьте, что страница загрузилась
print(f"Status Code: {response.status_code}")

# Печатаем все cookies, чтобы проверить, есть ли csrf_token
print(session.cookies.get_dict())  # Печатает все cookies из сессии

# Получаем csrf_token из cookies сессии
csrf_token = session.cookies.get('csrftoken')

if csrf_token:
    print(f"CSRF Token: {csrf_token}")
else:
    print("CSRF token not found.")
    exit(1)  # Прерываем выполнение, если токен не найден

# 2. Делаем POST-запрос с передачей CSRF токена в заголовке
headers = {
    'X-CSRFToken': csrf_token,  # Добавляем CSRF токен в заголовок
    'Content-Type': 'application/json',  # Тип данных
}

# Параметры для отправки в POST-запросе
data = {
    'name': 'Test Company',
    'email': 'test@mail.com',
    'password': 'testPassword123',
    'LLC_Number': '123456789',
}

# Отправляем POST-запрос с данными
response = session.post("http://127.0.0.1:8000/company/register/", headers=headers, json=data)

# Проверяем ответ
print(response.status_code)
print(response.json())  # Печатаем ответ от сервера в формате JSON
