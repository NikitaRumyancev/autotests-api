from httpx import Response
from typing import TypedDict, List
from clients.api_client import APIClient
from clients.privet_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа при создании упражнения.
    """
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа при
    """
    exercises: list[Exercise]


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры query params в запросе на получение списка заданий.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры тела запроса при отправке запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Структура ответа при создании задания.
    """
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры тела запроса при отправке запроса на частичное обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание сруктуры ответа при обновлении информации в задании.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Класс для работы с end-points:
    GET /api/v1/exercises. Получение списка заданий для определенного курса.
    GET /api/v1/exercises/{exercise_id}. Получение информации о задании по exercise_id.
    POST /api/v1/exercises. Создание задания.
    PATCH /api/v1/exercises/{exercise_id}. Обновления данных задания.
    DELETE /api/v1/exercises/{exercise_id}. Удаление задания.
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь c courseId.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url="/api/v1/exercises", params=query)

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод для запроса списка упражнений для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в формате json.
        """
        response = self.get_exercises_api(query=query)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании по exercise_id.

        :param exercise_id: Уникальный идентификатор.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод запроса информации о задании по exercise_id.

        :param exercise_id: Уникальный идентификатор упражнения.
        :return: Ответ от сервера в формате json.
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь из: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post(url="/api/v1/exercises", json=request)

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в формате json.
        """
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления данных задания.

        :param exercise_id: Уникальный идентификатор.
        :param request: Словарь из: title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод для обновления информации в задании.

        :param exercise_id: Уникальный идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в формате json.
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания по exercise_id.

        :param exercise_id: Уникальный идентификатор.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")


def get_private_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))