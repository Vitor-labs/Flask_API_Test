import requests

BASE = "http://127.0.0.1:5000/"
NEW_USER = {"username": "test_name",
            "email": "test@gmail.com",
            "fone": "123456789"}

response = requests.put(BASE + "user/1", json=NEW_USER)

print(response.status_code)
print(response.json())
