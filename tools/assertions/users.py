from typing import Any

from clients.users.user_schema import CreateUserResponseSchema, CreateUserRequestSchema, UserSchema
from tools.assertions.base import assert_equal
from clients.users.user_schema import GetUserResponseSchema
from fixtures.users import UserFixture
import allure
from tools.logger import get_logger


logger = get_logger("USERS_ASSERTIONS")


@allure.step("Assert create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema) -> None:
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Assert create user response")
    assert_equal(actual=response.user.email, expected=request.email, name="email")
    assert_equal(actual=response.user.first_name, expected=request.first_name, name="first_name")
    assert_equal(actual=response.user.middle_name, expected=request.middle_name, name="middle_name")
    assert_equal(actual=response.user.last_name, expected=request.last_name, name="last_name")

@allure.step("Assert user")
def assert_user(actual: UserSchema, expected: UserSchema) -> None:
    """
    Сравнивает два объекта UserSchema по всем полям.

    :param actual: объект UserSchema.
    :param expected: объект UserSchema.
    :raises: AssertionError Если хотя бы одно поле не совпадает.
    """
    logger.info("Assert user")
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.email, expected=expected.email, name="email")
    assert_equal(actual=actual.first_name, expected=expected.first_name, name="first_name")
    assert_equal(actual=actual.middle_name, expected=expected.middle_name, name="middle_name")
    assert_equal(actual=actual.last_name, expected=expected.last_name, name="last_name")

@allure.step("Assert get user response")
def assert_get_user_response(get_user_response: Any, create_user_response: UserFixture) -> None:
    """
    Проверяет, что данные пользователя при запросе соответствуют данным при создании.

    :param get_user_response: Ответ от сервера при запросе пользователя.
    :param create_user_response: Ответ от сервера при создании пользователя.
    :raises: AssertionError в случае, если найдено несовпадение по полям.
    """
    logger.info("Assert get user response")
    get_user_response = GetUserResponseSchema.model_validate_json(get_user_response.text)
    assert_user(actual=get_user_response.user, expected=create_user_response.response.user)
