from http import HTTPStatus

import pytest
from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCoursesRequestSchema, UpdateCourseResponseSchema
from clients.courses.courses_schema import GetCoursesQuerySchema, GetCoursesResponseSchema
from clients.courses.courses_schema import CreateCoursesRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_course_update_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:

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

    def test_update_course(self,
                           course_client: CoursesClient,
                           function_course: CourseFixture):
        request = UpdateCoursesRequestSchema()
        response = course_client.update_course_api(course_id=function_course.course_id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_course_update_response(request=request, response=response_data)

        validate_json_schema(instance=response.json(), schema=UpdateCourseResponseSchema.model_json_schema())
