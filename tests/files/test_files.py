from http import HTTPStatus

import allure
import pytest
from clients.files.file_schema import CreateFileResponseSchema, CreateFileRequestSchema, GetFileResponseSchema
from clients.files.files_client import FilesClient
from clients.errors_schemas import ValidationErrorResponseSchema
from clients.errors_schemas import InternalErrorResponseSchema
from fixtures.files import FileFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_get_file_response, \
    assert_create_file_with_empty_directory_response, assert_create_file_with_empty_filename_response, \
    assert_file_not_found, assert_get_file_with_incorrect_file_id_response
from tools.assertions.schema import validate_json_schema
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
from config import settings


@pytest.mark.files
@pytest.mark.regression
@allure.tag(AllureTag.FILES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.FILES)
@allure.suite(AllureFeature.FILES)
class TestFiles:
    """
    Тестовый класс для тестирования функциональной области (Работа с файлами)
    """

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Create file")
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
        response = files_client.create_file_api(request=request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_file_response(request=request, response=response_data)

        validate_json_schema(instance=response.json(), schema=CreateFileResponseSchema.model_json_schema())

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get file")
    def test_get_file(self, function_file: FileFixture, files_client: FilesClient):
        response = files_client.get_file_api(file_id=function_file.file_id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_file_response(get_file_response=response_data,
                                 create_file_response=function_file.response)

        validate_json_schema(instance=response.json(), schema=GetFileResponseSchema.model_json_schema())

    @allure.severity(Severity.NORMAL)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.title("Create file with empty directory")
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            directory="",
            upload_file=settings.test_data.image_png_file
        )
        response = files_client.create_file_api(request)
        request_error = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(request_error)

        validate_json_schema(instance=response.json(), schema=ValidationErrorResponseSchema.model_json_schema())

    @allure.severity(Severity.NORMAL)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.title("Create file with empty filename")
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file=settings.test_data.image_png_file)
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)

        validate_json_schema(instance=response.json(), schema=ValidationErrorResponseSchema.model_json_schema())

    @allure.severity(Severity.NORMAL)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("Delete file")
    def test_delete_file(self, files_client: FilesClient, function_file: FileFixture):
        delete_file_response = files_client.delete_file_api(file_id=function_file.file_id)

        assert_status_code(delete_file_response.status_code, HTTPStatus.OK)

        get_file_response = files_client.get_file_api(file_id=function_file.file_id)
        get_file_response_data = InternalErrorResponseSchema.model_validate_json(get_file_response.text)

        assert_file_not_found(actual=get_file_response_data)

        validate_json_schema(instance=get_file_response.json(), schema=InternalErrorResponseSchema.model_json_schema())

    @allure.severity(Severity.NORMAL)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.VALIDATE_ENTITY)
    @allure.title("Get file with incorrect file id")
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        get_file_response = files_client.get_file_api(file_id="incorrect-file-id")

        get_file_response_data = ValidationErrorResponseSchema.model_validate_json(get_file_response.text)

        assert_status_code(get_file_response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(actual=get_file_response_data)

        validate_json_schema(instance=get_file_response.json(),
                             schema=ValidationErrorResponseSchema.model_json_schema())
