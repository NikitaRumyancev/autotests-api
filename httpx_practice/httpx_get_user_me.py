import httpx

LOGIN_URL = "http://localhost:8000/api/v1/authentication/login"
URL_GET_USER_ME = "http://localhost:8000/api/v1/users/me"

login_payload_user_data = {
    "email": "user@example.com",
    "password": "string",
}


response = httpx.post(url=LOGIN_URL, json=login_payload_user_data)

access_user_token = response.json()["token"]["accessToken"]

auth_data = {
  "Authorization": f"Bearer {access_user_token}"
}

response = httpx.get(url=URL_GET_USER_ME, headers=auth_data)
print(f"Response status code = {response.status_code}\n"
      f"{response.json()}")


