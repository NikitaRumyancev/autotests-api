from clients.users.user_schema import CreateUserResponseSchema, CreateUserRequestSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=response.user.email, expected=request.email, name="email")
    assert_equal(actual=response.user.first_name, expected=request.first_name, name="first_name")
    assert_equal(actual=response.user.middle_name, expected=request.middle_name, name="middle_name")
    assert_equal(actual=response.user.last_name, expected=request.last_name, name="last_name")