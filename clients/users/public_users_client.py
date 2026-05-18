from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.user_schema import (CreateUserRequestSchema,
                                       CreateUserResponseSchema)


class PublicUsersClient(APIClient):
    """
    Клиент для работы с  /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод для создания нового пользователя.
        :param request: Словарь с необходимыми полями для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post(url="/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Метод для создания пользователя и получения ответа от сервера в виде json.
        :param request:  Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде json.
        """
        response = self.create_user_api(request=request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_user_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
