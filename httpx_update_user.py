import httpx
from tools.fackers import get_random_email_for_user

post_request_headers = {"accept": "application/json",
                        "Content-Type": "application/json"}

post_request_payload = {
  "email": f"{get_random_email_for_user()}",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

post_response = httpx.post(url="http://localhost:8000/api/v1/users",
                           json=post_request_payload,
                           headers=post_request_headers)
print(post_response.json())

login_payload = {
    "email": f"{post_request_payload["email"]}",
    "password": f"{post_request_payload["password"]}"
}

login_response = httpx.post(url="http://localhost:8000/api/v1/authentication/login",
                            json=login_payload,
                            headers={"accept": "application/json",
                                     "Content-Type": "application/json"})
print(login_response.json())

response_get_user_by_id = httpx.get(url=f"http://localhost:8000/api/v1/users/{post_response.json()["user"]["id"]}",
                                    headers={f"Authorization": f"Bearer {login_response.json()["token"]["accessToken"]}"})
print(response_get_user_by_id.json())