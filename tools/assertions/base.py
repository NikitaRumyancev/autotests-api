from typing import Any, Sized
import allure
from tools.logger import get_logger

logger = get_logger("BASE_ASSERTION")


@allure.step("Assert status code. actual: {actual}, expected: {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Метод проверяет, что фактических статус код и ожидаемых совпадают.

    :param actual: Фактический статус код.
    :param expected: Ожидаемый статус код.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    logger.info(f"Assert status code. actual: {actual}, expected: {expected}")
    assert actual == expected, (
        "Incorrect status code. "
        f"Expected status code: {expected}. "
        f"Actual status code: {actual}. "
    )


@allure.step("Assert that actual value: {actual} equals expected value: {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

   :param name: Название проверяемого значения.
   :param actual: Фактическое значение.
   :param expected: Ожидаемое значение.
   :raises AssertionError: Если фактическое значение не равно ожидаемому.
   """
    logger.info(f"Assert that actual value: {actual} equals expected value: {expected}")
    assert actual == expected, (
        f"Incorrect value {name}. "
        f"Expected value: {expected}. "
        f"Actual value: {actual}. "
    )


@allure.step("Assert that actual value is True")
def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    logger.info("Assert that actual value is True.")
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


@allure.step("Assert that actual length value equals expected")
def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    logger.info(f"Assert that actual length value equals expected.")
    assert len(actual) == len(expected), (
        f"Incorrect objects length: {name}. "
        f"Expected length: {len(expected)}. "
        f"Actual length: {len(actual)}. "
    )
