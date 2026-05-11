from clients.public_http_builder import get_public_http_client
from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class Token(TypedDict):
    """
    Структура токена.
    """
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginResponseDict(TypedDict):
    """
    Структура ответа от сервера при успешной аутентификации.
    """
    token: Token


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    pass

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        Метод аутентификации пользователя и получения ответа от сервера в виде json.

        :param request: Словарь с email, password.
        :return: Ответ от сервера в формате json.
        """
        login_response = self.login_api(request)
        return login_response.json()

def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())