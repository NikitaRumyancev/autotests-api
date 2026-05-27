import pytest

from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.authentication.authentication_client import AuthenticationClient
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from http import HTTPStatus
from fixtures.users import UserFixture


class TestAuthentication:


    @pytest.mark.regression
    @pytest.mark.authentication
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):
        login_request = authentication_client.login_api(request=LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        ))
        response_data = LoginResponseSchema.model_validate_json(login_request.text)

        assert_status_code(actual=login_request.status_code, expected=HTTPStatus.OK)
        assert_login_response(response=response_data)

        validate_json_schema(instance=response_data.model_dump(by_alias=True),
                             schema=LoginResponseSchema.model_json_schema())





