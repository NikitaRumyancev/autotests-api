from authentication.authentication_schemа import (LoginRequestSchema,
                                                  LoginResponseSchema,
                                                  RefreshRequestSchema)
from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """


    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/authentication/login", json=request.model_dump())

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Метод аутентификации пользователя и получения ответа от сервера в виде json.

        :param request: Словарь с email, password.
        :return: Ответ от сервера в формате json.
        """
        login_response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(login_response.text)

def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())