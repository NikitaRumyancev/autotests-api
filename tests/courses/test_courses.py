from http import HTTPStatus

import allure
import pytest
from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCoursesRequestSchema, UpdateCourseResponseSchema
from clients.courses.courses_schema import GetCoursesQuerySchema, GetCoursesResponseSchema
from clients.courses.courses_schema import CreateCoursesRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_course_update_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema
from tools.allure.tags import AllureTag
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.suite(AllureFeature.COURSES)
class TestCourses:
    """
    Тестовый класс для тестирования сценариев связанных с курсами.
    """

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Create course")
    def test_create_course(self,
                           course_client: CoursesClient,
                           function_user: UserFixture,
                           function_file: FileFixture):
        request = CreateCoursesRequestSchema(
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id)
        response = course_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_course_response(actual=response_data, expected=request)

        validate_json_schema(instance=response.json(), schema=CreateCourseResponseSchema.model_json_schema())

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("Get courses")
    def test_get_courses(self,
                         course_client: CoursesClient,
                         function_course: CourseFixture,
                         function_user: UserFixture):
        query = GetCoursesQuerySchema(userId=function_user.user_id)
        response = course_client.get_course_api(query=query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])

        validate_json_schema(instance=response.json(), schema=GetCoursesResponseSchema.model_json_schema())

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("Update course")
    def test_update_course(self,
                           course_client: CoursesClient,
                           function_course: CourseFixture):
        request = UpdateCoursesRequestSchema()
        response = course_client.update_course_api(course_id=function_course.course_id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_course_update_response(request=request, response=response_data)

        validate_json_schema(instance=response.json(), schema=UpdateCourseResponseSchema.model_json_schema())
