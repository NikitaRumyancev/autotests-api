import pytest
from clients.courses.courses_client import CoursesClient, get_private_course_client
from clients.courses.courses_schema import CreateCoursesRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from pydantic import BaseModel


class CourseFixture(BaseModel):
    """
    Pydantic-модель, объединяющая запрос и ответ при создании курса.
    """
    request: CreateCoursesRequestSchema
    response: CreateCourseResponseSchema

    @property
    def course_id(self):
        return self.response.course.id


@pytest.fixture
def course_client(function_user: UserFixture) -> CoursesClient:
    """
    Фикстура для инциализации клиента для работы с курсами (CoursesClient).

    :param function_user: Фистура для создания пользователя.
    :return: Настроенный клиент для работы с курсами (CoursesClient).
    """
    return get_private_course_client(user=function_user.authentication_user)

@pytest.fixture
def function_course(
        course_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture) -> CourseFixture:
    """
    Фистура для создания курса.

    :param course_client: Фикстура для инциализации клиента для работы с курсами (CoursesClient).
    :param function_user: Фикстура для создания пользователя.
    :param function_file: Фикстура для создания файла.
    :return: Pydantic-модель, объединяющая запрос и ответ при создании курса.
    """
    request = CreateCoursesRequestSchema(
        createdByUserId=function_user.user_id,
        previewFileId=function_file.file_id)
    response = course_client.create_course(request=request)
    return CourseFixture(request=request, response=response)