from clients.users.public_users_client import get_public_user_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.user_schema import  CreateUserRequestSchema
from clients.authentication.authentication_client import get_authentication_client
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from http import HTTPStatus


class TestAuthentication:


    def test_login(self):
        user_client = get_public_user_client()
        auth_client = get_authentication_client()
        request = CreateUserRequestSchema()
        user_client.create_user(request=request)
        login_response  = auth_client.login_api(request=LoginRequestSchema(
            email=request.email,
            password=request.password
        ))
        login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
        assert_status_code(actual=login_response.status_code, expected=HTTPStatus.OK)
        assert_login_response(response=login_response_data)
        validate_json_schema(instance=login_response_data.model_dump(by_alias=True),
                             schema=LoginResponseSchema.model_json_schema())





