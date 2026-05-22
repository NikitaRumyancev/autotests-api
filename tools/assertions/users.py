from clients.users.user_schema import CreateUserResponseSchema, CreateUserRequestSchema
from tools.assertions.base import assert_equals


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    assert_equals(actual=response.user.email, expected=request.email, name="email")
    assert_equals(actual=response.user.first_name, expected=request.first_name, name="first_name")
    assert_equals(actual=response.user.middle_name, expected=request.middle_name, name="middle_name")
    assert_equals(actual=response.user.last_name, expected=request.last_name, name="last_name")