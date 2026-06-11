from clients.courses.courses_schema import (CreateCourseResponseSchema,
                                    CreateCoursesRequestSchema,
                                    UpdateCoursesRequestSchema)
from httpx import Response

from clients.api_client import APIClient
from clients.privet_http_builder import (AuthenticationUserSchema,
                                         get_private_http_client)
from clients.courses.courses_schema import GetCoursesQuerySchema
import allure
from tools.routers import APIRouters


class CoursesClient(APIClient):
    """
    Класс для работы с end-points:
    GET: /api/v1/courses
    POST: /api/v1/courses
    GET: /api/v1/courses/{course_id}
    PATCH: /api/v1/courses/{course_id}
    DELETE: /api/v1/courses/{course_id}
    """


    @allure.step("Get course using query params")
    def get_course_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь query параметров с userId.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=f"{APIRouters.COURSES}", params=query.model_dump(by_alias=True))

    @allure.step("Create course")
    def create_course_api(self, request: CreateCoursesRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в виде json
        """
        return self.post(url=f"{APIRouters.COURSES}", json=request.model_dump(by_alias=True))

    def create_course(self, request: CreateCoursesRequestSchema) -> CreateCourseResponseSchema:
        """
        Метод для создания курса и конвертации ответа в json формат.

        :param request: Словарь title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в формате json.
        """
        response = self.create_course_api(request=request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    @allure.step("Get course by id: {course_id}")
    def get_course_by_id(self, course_id: str) -> Response:
        """
        Метод получения курса по уникальному идентификатору.

        :param course_id: Уникальный идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"{APIRouters.COURSES}/{course_id}")

    @allure.step("Update course by id: {course_id}")
    def update_course_api(self, course_id: str, request: UpdateCoursesRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"{APIRouters.COURSES}/{course_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete course by id: {course_id}")
    def delete_courses_api(self, course_id: str) -> Response:
        """
        Метод удаления курса по уникальному идентификатору.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(url=f"{APIRouters.COURSES}/{course_id}")

@allure.step("Initialization course client")
def get_private_course_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))