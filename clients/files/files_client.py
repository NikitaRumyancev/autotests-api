from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.privet_http_builder import AuthenticationUserDict, get_private_http_client


class File(TypedDict):
    """
    Описание структуры файла.
    """
    id: str
    filename: str
    directory: str
    url: str


class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа при успешном создании файла.
    """
    file: File


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """
    Класс для работы с end-points:
    GET: /api/v1/files/{file_id}
    DELETE: /api/v1/files/{file_id}
    POST: /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f"/api/v1/files",
            data=request,
            files={f"upload_file": open(request["upload_file"], "rb")})

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        """
        Метод создания файла и получения ответа от сервера в виде json.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в формате json.
        """
        response = self.create_file_api(request=request)
        return response.json()

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/files/{file_id}")


def get_private_file_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))