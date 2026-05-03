from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


class CreateUserPayloadDict(TypedDict):
    """
    Описание структуры тела запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с  /api/v1/users
    """
    def create_user_api(self, request_payload: CreateUserPayloadDict) -> Response:
        """
        Метод для создания нового пользователя.
        :param request_payload: Словарь с необходимыми полями для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post(url="/api/v1/users", json=request_payload)
