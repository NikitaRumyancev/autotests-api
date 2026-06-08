import allure
import pytest

from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.authentication.authentication_client import AuthenticationClient
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from http import HTTPStatus
from fixtures.users import UserFixture
from tools.allure.tags import AllureTag
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTag.AUTHENTICATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    """
    Тестовый класс для тестирования сценариев связанных с аутентификацией.
    """

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.LOGIN)
    @allure.sub_suite(AllureStory.LOGIN)
    @allure.title("Login user")
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
