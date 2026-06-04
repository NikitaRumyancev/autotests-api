from clients.courses.courses_schema import UpdateCourseResponseSchema, UpdateCoursesRequestSchema, CourseSchema
from clients.courses.courses_schema import GetCoursesResponseSchema, CreateCourseResponseSchema
from clients.courses.courses_schema import CreateCoursesRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user

def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.title, expected=expected.title, name="title")
    assert_equal(actual=actual.max_score, expected=expected.max_score, name="max_score")
    assert_equal(actual=actual.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.description, expected=expected.description, name="description")
    assert_equal(actual=actual.estimated_time, expected=expected.estimated_time, name="estimated_time")

    assert_file(actual=actual.preview_file, expected=expected.preview_file)
    assert_user(actual=actual.created_by_user, expected=expected.created_by_user)

def assert_create_course_response(actual: CreateCourseResponseSchema, expected: CreateCoursesRequestSchema):
    """
    Метод проверяет, что информация в ответе при создании курса соответствует информации в запросе на создание кусра.

    :param actual: Фактические данные в ответе.
    :param expected: Ожидаемые данные в ответе.
    :raises:  AssertionError, если хотя бы одно поле не совпадает с ожидаемым.
    """
    assert_equal(actual=actual.course.title, expected=expected.title, name="title")
    assert_equal(actual=actual.course.max_score, expected=expected.max_score, name="max_score")
    assert_equal(actual=actual.course.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.course.description, expected=expected.description, name="description")
    assert_equal(actual=actual.course.estimated_time, expected=expected.estimated_time, name="estimated_time")
    assert_equal(actual=actual.course.preview_file.id, expected=expected.preview_file_id, name="preview_file_id")
    assert_equal(actual=actual.course.created_by_user.id, expected=expected.created_by_user_id, name="preview_file_id")

def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_response: list[CreateCourseResponseSchema]):
    """
   Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

   :param get_courses_response: Ответ API при запросе списка курсов.
   :param create_course_response: Список API ответов при создании курсов.
   :raises AssertionError: Если данные курсов не совпадают.
   """
    assert_length(actual=get_courses_response.courses, expected=create_course_response, name="courses")

    for index, create_course_response in enumerate(create_course_response):
        assert_course(actual=get_courses_response.courses[index], expected=create_course_response.course)

def assert_course_update_response(request: UpdateCoursesRequestSchema, response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=request.title, expected=response.course.title, name="title")
    assert_equal(actual=request.max_score, expected=response.course.max_score, name="max_score")
    assert_equal(actual=request.min_score, expected=response.course.min_score, name="min_score")
    assert_equal(actual=request.description, expected=response.course.description, name="description")
    assert_equal(actual=request.estimated_time, expected=response.course.estimated_time, name="estimated_time")