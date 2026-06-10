from clients.files.file_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema, \
    FileSchema
from clients.errors_schemas import InternalErrorResponseSchema

from tools.assertions.base import assert_equal
from clients.errors_schemas import ValidationErrorResponseSchema, ValidationErrorSchema
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
import allure
from config import settings


@allure.step("Assert create file response")
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, фактические и ожидаемые данные в ответе от сервера после создания файла.

    :param request: Ожидамые данные.
    :param response: Фактические данные.
    :raises: AssertionError в случае несовпадения ожидаемых и фактических данных.
    """
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"

    assert_equal(actual=response.file.filename, expected=request.filename, name="filename")
    assert_equal(actual=response.file.directory, expected=request.directory, name="directory")
    assert_equal(actual=str(response.file.url), expected=expected_url, name="url")


@allure.step("Assert file")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.filename, expected=expected.filename, name="filename")
    assert_equal(actual=actual.directory, expected=expected.directory, name="directory")
    assert_equal(actual=actual.url, expected=expected.url, name="url")


@allure.step("Assert get file response")
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание.

    :param get_file_response: Ответ API при запросе данных файла.
    :param create_file_response: Ответ API при создании файла.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_file(actual=get_file_response.file, expected=create_file_response.file)


@allure.step("Assert create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                location=["body", "filename"],
                msg="String should have at least 1 character",
                input="",
                context={"min_length": 1}
            )

        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Assert create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                location=["body", "directory"],
                msg="String should have at least 1 character",
                input="",
                context={"min_length": 1}
            )

        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Assert file not found")
def assert_file_not_found(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(
        detail="File not found"
    )
    assert_internal_error_response(actual, expected)


@allure.step("Assert get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Функция проверяет, что при выполнеии get запроса на получение файла по file_id ответ от сервера соответствует
    ожидаемой валидационной ошибке.

    :param actual: Структура ожидаемой валидационной ошибки.
    :raises: AssertionError если хотя бы одно поле не совпадает.
    """
    expected = ValidationErrorResponseSchema(
        detail=[ValidationErrorSchema(
            type="uuid_parsing",
            location=["path", "file_id"],
            message=(
                "Input should be a valid UUID, "
                "invalid character: expected an optional prefix of `urn:uuid:` "
                "followed by [0-9a-fA-F-], found `i` at 1"
            ),
            input="incorrect-file-id",
            context={"error": ("invalid character: expected an optional prefix of `urn:uuid:` "
                               "followed by [0-9a-fA-F-], found `i` at 1")}
        )]
    )
    assert_validation_error_response(actual, expected)
