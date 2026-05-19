from pydantic_core.core_schema import json_schema
from jsonschema import validate

from users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.users.public_users_client import get_public_user_client
from tools.fakers import Fakers
from tools.assertions.schema import validate_json_schema

public_users_client = get_public_user_client()

request_data = CreateUserRequestSchema(
    email=f'{Fakers.get_random_email_for_user()}',
    password='12345',
    lastName='Nikita',
    firstName='Nikita',
    middleName='Nikita')

create_user_response = public_users_client.create_user_api(request=request_data)

json_data = create_user_response.json()

json_data["user"]["email"] = "test"

json_schema_1 = CreateUserResponseSchema.model_json_schema()


validate_json_schema(instance=json_data, schema=json_schema_1)
"""
json_schema_1 = {'$defs': {'UserSchema': {'description': 'Описание структуры пользователя.',
                              'properties': {'id': {'title': 'Id', 'type': 'string'},
                                             'email': {'format': 'email', 'title': 'Email', 'type': 'string'},
                                             'lastName': {'title': 'Lastname', 'type': 'string'},
                                             'firstName': {'title': 'Firstname', 'type': 'string'},
                                             'middleName': {'title': 'Middlename', 'type': 'string'}},
                              'required': ['id', 'email', 'lastName', 'firstName', 'middleName'], 'title': 'UserSchema',
                              'type': 'object'}}, 'description': 'Описание структуры ответа создания пользователя.',
     'properties': {'user': {'$ref': '#/$defs/UserSchema'}}, 'required': ['user'], 'title': 'CreateUserResponseSchema',
     'type': 'object'}
"""

