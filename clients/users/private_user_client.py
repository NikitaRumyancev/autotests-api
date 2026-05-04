from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры тела запроса для частичного обновления пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    """
    Класс для работы с end-poins которые требуют аутентификации:
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

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод частичного обновления пользователя.
        :param user_id: Уникальный идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        Можно выбрать опционально какое то одно поле.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.patch(url=f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по уникальному идентификатору.
        :param user_id: Уникальный идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/users/{user_id}")