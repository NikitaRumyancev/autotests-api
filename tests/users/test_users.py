import pytest

from clients.users.public_users_client import PublicUsersClient
from http import HTTPStatus
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
class TestUsers:

    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self,
                         public_user_client: PublicUsersClient,
                         domain: str):
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        response = public_user_client.create_user_api(request=request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_user_response(request=request, response=response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_get_user_me(self,
                         private_user_client,
                         function_user):
        create_user_response = function_user
        get_user_me_response = private_user_client.get_user_me_api()

        assert_status_code(actual=get_user_me_response.status_code, expected=HTTPStatus.OK)
        assert_get_user_response(get_user_me_response, create_user_response)

        validate_json_schema(instance=get_user_me_response.json(), schema=GetUserResponseSchema.model_json_schema())
