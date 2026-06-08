import allure
import pytest

from clients.users.public_users_client import PublicUsersClient
from http import HTTPStatus
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.allure.tags import AllureTag
from tools.fakers import fake
from allure_commons.types import Severity


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.suite(AllureFeature.USERS)
class TestUsers:

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Create user")
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self,
                         public_user_client: PublicUsersClient,
                         domain: str):
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        response = public_user_client.create_user_api(request=request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_user_response(request=request, response=response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get user me")
    def test_get_user_me(self,
                         private_user_client,
                         function_user):
        create_user_response = function_user
        get_user_me_response = private_user_client.get_user_me_api()

        assert_status_code(actual=get_user_me_response.status_code, expected=HTTPStatus.OK)
        assert_get_user_response(get_user_me_response, create_user_response)

        validate_json_schema(instance=get_user_me_response.json(), schema=GetUserResponseSchema.model_json_schema())
