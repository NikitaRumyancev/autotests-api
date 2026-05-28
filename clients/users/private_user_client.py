from httpx import Response
from clients.privet_http_builder import AuthenticationUserSchema
from clients.users.user_schema import GetUserResponseSchema, UpdateUserRequestSchema

from clients.api_client import APIClient
from clients.privet_http_builder import get_private_http_client


class PrivateUsersClient(APIClient):
    """
    Класс для работы с end-points которые требуют аутентификации:
    GET: /api/v1/users/me
    GET: /api/v1/users/{user_id}
    PATCH: /api/v1/users/{user_id}
    DELETE: /api/v1/users/{user_id}
    """

    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url="/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по уникальному идентификатору.
        :param user_id: Уникальный идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id=user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод частичного обновления пользователя.
        :param user_id: Уникальный идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        Можно выбрать опционально какое то одно поле.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.patch(url=f"/api/v1/users/{user_id}", json=request.model_dump())

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по уникальному идентификатору.
        :param user_id: Уникальный идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/users/{user_id}")


def get_private_user_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))