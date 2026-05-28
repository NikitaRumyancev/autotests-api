from clients.exercises.exercises_shema import (CreateExerciseRequestSchema,
                                       CreateExerciseResponseSchema,
                                       GetExerciseResponseSchema,
                                       GetExercisesQuerySchema,
                                       GetExercisesResponseSchema,
                                       UpdateExerciseRequestSchema,
                                       UpdateExerciseResponseSchema)
from httpx import Response

from clients.api_client import APIClient
from clients.privet_http_builder import (AuthenticationUserSchema,
                                         get_private_http_client)


class ExercisesClient(APIClient):
    """
    Класс для работы с end-points:
    GET /api/v1/exercises. Получение списка заданий для определенного курса.
    GET /api/v1/exercises/{exercise_id}. Получение информации о задании по exercise_id.
    POST /api/v1/exercises. Создание задания.
    PATCH /api/v1/exercises/{exercise_id}. Обновления данных задания.
    DELETE /api/v1/exercises/{exercise_id}. Удаление задания.
    """
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь c courseId.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url="/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод для запроса списка упражнений для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в формате json.
        """
        response = self.get_exercises_api(query=query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании по exercise_id.

        :param exercise_id: Уникальный идентификатор.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод запроса информации о задании по exercise_id.

        :param exercise_id: Уникальный идентификатор упражнения.
        :return: Ответ от сервера в формате json.
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь из: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post(url="/api/v1/exercises", json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в формате json.
        """
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления данных задания.

        :param exercise_id: Уникальный идентификатор.
        :param request: Словарь из: title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод для обновления информации в задании.

        :param exercise_id: Уникальный идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в формате json.
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания по exercise_id.

        :param exercise_id: Уникальный идентификатор.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")


def get_private_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))