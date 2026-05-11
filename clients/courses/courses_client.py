from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.files.files_client import File
from clients.privet_http_builder import get_private_http_client
from clients.privet_http_builder import AuthenticationUserDict
from clients.users.private_user_client import User


class Course(TypedDict):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User


class CreateCourseResponseDict(TypedDict):
    """
    Описание структуры ответа создания курса.
    """
    course: Course


class CreateCoursesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCoursesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class CoursesClient(APIClient):
    """
    Класс для работы с end-points:
    GET: /api/v1/courses
    POST: /api/v1/courses
    GET: /api/v1/courses/{course_id}
    PATCH: /api/v1/courses/{course_id}
    DELETE: /api/v1/courses/{course_id}
    """


    def get_course_api(self, query: str) -> Response:
        """
        Метод получения списка курсов.
        :param query: Словарь query параметров с userId.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url="/api/v1/courses", params=query)

    def create_course_api(self, request: CreateCoursesRequestDict) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в виде json
        """
        return self.post(url="/api/v1/courses", json=request)

    def create_course(self, request: CreateCoursesRequestDict) -> CreateCourseResponseDict:
        """
        Метод для создания курса и конвертации ответа в json формат.

        :param request: Словарь title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в формате json.
        """
        response = self.create_course_api(request=request)
        return response.json()

    def get_course_by_id(self, course_id: str) -> Response:
        """
        Метод получения курса по уникальному идентификатору.
        :param course_id: Уникальный идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCoursesRequestDict) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/courses/{course_id}", json=request)

    def delete_courses_api(self, course_id: str) -> Response:
        """
        Метод удаления курса по уникальному идентификатору.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(url=f"/api/v1/courses/{course_id}")

def get_private_course_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))