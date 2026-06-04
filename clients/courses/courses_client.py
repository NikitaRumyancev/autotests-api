from clients.courses.courses_schema import (CreateCourseResponseSchema,
                                    CreateCoursesRequestSchema,
                                    UpdateCoursesRequestSchema)
from httpx import Response

from clients.api_client import APIClient
from clients.privet_http_builder import (AuthenticationUserSchema,
                                         get_private_http_client)
from clients.courses.courses_schema import GetCoursesQuerySchema


class CoursesClient(APIClient):
    """
    Класс для работы с end-points:
    GET: /api/v1/courses
    POST: /api/v1/courses
    GET: /api/v1/courses/{course_id}
    PATCH: /api/v1/courses/{course_id}
    DELETE: /api/v1/courses/{course_id}
    """


    def get_course_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь query параметров с userId.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url="/api/v1/courses", params=query.model_dump(by_alias=True))

    def create_course_api(self, request: CreateCoursesRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в виде json
        """
        return self.post(url="/api/v1/courses", json=request.model_dump(by_alias=True))

    def create_course(self, request: CreateCoursesRequestSchema) -> CreateCourseResponseSchema:
        """
        Метод для создания курса и конвертации ответа в json формат.

        :param request: Словарь title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в формате json.
        """
        response = self.create_course_api(request=request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def get_course_by_id(self, course_id: str) -> Response:
        """
        Метод получения курса по уникальному идентификатору.

        :param course_id: Уникальный идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCoursesRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_courses_api(self, course_id: str) -> Response:
        """
        Метод удаления курса по уникальному идентификатору.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(url=f"/api/v1/courses/{course_id}")

def get_private_course_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))