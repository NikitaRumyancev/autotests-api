from clients.users.private_user_client import (AuthenticationUserSchema,
                                               get_private_user_client)
from clients.users.public_users_client import get_public_user_client
from clients.users.user_schema import (CreateUserRequestSchema,
                                       GetUserResponseSchema)
from tools.assertions.schema import validate_json_schema
from tools.fakers import Fakers as fk

request_create_user_data = {
    "email": f"{fk.get_random_email_for_user()}",
    "password": "12345",
    "last_name": "last_name",
    "first_name": "first_name",
    "middle_name": "middle_name"
}

create_user_schema = CreateUserRequestSchema.model_validate(request_create_user_data)

auth_user_data = {
    "email": f"{create_user_schema.email}",
    "password": f"{create_user_schema.password}"
}

public_user_client = get_public_user_client()

create_user_response = public_user_client.create_user(
    request=create_user_schema)

private_user_client = get_private_user_client(user=AuthenticationUserSchema(email=create_user_schema.email,
                                                                            password=create_user_schema.password))

get_user_response = private_user_client.get_user_api(user_id=create_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)
