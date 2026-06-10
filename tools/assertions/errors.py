from clients.errors_schemas import ValidationErrorResponseSchema, ValidationErrorSchema
from clients.errors_schemas import InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
import allure
from tools.logger import get_logger


logger = get_logger("ERRORS_ASSERTION")


@allure.step("Assert validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """
    logger.info("Assert validation error.")
    assert_equal(actual=actual.type, expected=expected.type, name="type")
    assert_equal(actual=actual.location, expected=expected.location, name="location")
    assert_equal(actual=actual.message, expected=expected.message, name="message")
    assert_equal(actual=actual.input, expected=expected.input, name="input")
    assert_equal(actual=actual.context, expected=expected.context, name="context")


@allure.step("Assert validation error response")
def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    """
    Проверяет, что объект ответа API с ошибками валидации (`ValidationErrorResponseSchema`)
    соответствует ожидаемому значению.

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_length(actual=actual.details, expected=expected.details, name="detail")

    logger.info("Assert validation error response.")
    for index, detail in enumerate(expected.details):
        assert_validation_error(actual=actual.details[index], expected=detail)

@allure.step("Assert internal error response")
def assert_internal_error_response(actual: InternalErrorResponseSchema, expected: InternalErrorResponseSchema):
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    logger.info("Assert internal error response.")
    assert_equal(actual=actual.details, expected=expected.details, name="detail")

