from clients.users.public_users_client import get_public_user_client
from http import HTTPStatus
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response


class TestUserAuthentication:

    def test_create_user(self):
        user_client = get_public_user_client()
        request = CreateUserRequestSchema()
        response = user_client.create_user_api(request=request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_user_response(request=request, response=response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())








