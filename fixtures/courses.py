import pytest
from clients.courses.courses_client import CoursesClient, get_private_course_client
from clients.courses.courses_schema import CreateCoursesRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from pydantic import BaseModel


class CourseFixture(BaseModel):
    request: CreateCoursesRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def course_client(function_user: UserFixture) -> CoursesClient:
    return get_private_course_client(user=function_user.authentication_user)

@pytest.fixture
def function_course(
        course_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture) -> CourseFixture:
    request = CreateCoursesRequestSchema()
    response = course_client.create_course(request=request)
    return CourseFixture(request=request, response=response)