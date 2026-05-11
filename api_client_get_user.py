from clients.users.public_users_client import get_public_user_client, CreateUserRequestDict
from clients.users.private_user_client import AuthenticationUserDict, get_private_user_client
from tools.fakers import Fakers

public_users_client = get_public_user_client()

request_data = CreateUserRequestDict(
    email=f'{Fakers.get_random_email_for_user()}',
    password='12345',
    lastName='Nikita',
    firstName='Nikita',
    middleName='Nikita')

create_user_response = public_users_client.create_user(request=request_data)

authentication_user = AuthenticationUserDict(
    email=request_data['email'],
    password=request_data['password'])

private_user_client = get_private_user_client(user=authentication_user)
get_user_response = private_user_client.get_user(user_id=create_user_response["user"]["id"])

print(f"Create user response data: {create_user_response}")

print(f"Get user response data: {get_user_response}")





