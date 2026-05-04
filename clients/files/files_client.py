import httpx

from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


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

    def create_file_api(self, request: TypedDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f"/api/v1/files",
            data=request,
            files={f"upload_file": open(request["upload_file"], "rb")})

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/files/{file_id}")
