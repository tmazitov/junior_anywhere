#!/bin/bash

# URL, на который отправляется POST-запрос
URL="http://127.0.0.1:8000/company/register/"

# Данные для создания новой компании в формате JSON
JSON_DATA='{
  "name": "Test Company",
  "password": "password123",     # Пароль должен содержать хотя бы одну букву, одну цифру и минимум 8 символов
  "email": "testcompany@mail.com",
  "LLC_Number": "123456789"
}'

# Выполнение POST-запроса
echo "Sending POST request to $URL with JSON data..."
curl -X POST -H "Content-Type: application/json" -d "$JSON_DATA" $URL

echo "Request sent."
