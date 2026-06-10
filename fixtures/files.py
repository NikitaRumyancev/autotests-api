import pytest
from clients.files.files_client import get_private_file_client, FilesClient
from clients.files.file_schema import CreateFileRequestSchema, CreateFileResponseSchema
from pydantic import BaseModel
from config import settings

from fixtures.users import UserFixture


class FileFixture(BaseModel):
    """
    Pydantic-модель, объединяющая запрос и ответ при создании файла.
    """
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

    @property
    def file_id(self):
        return self.response.file.id

@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    """
    Фикстура для инициализации клиента для работы с файлами (FilesClient).

    :param function_user: Фикстура для создания пользователя.
    :return: Настроенный клиент для работы с файлами (FilesClient).
    """
    return get_private_file_client(user=function_user.authentication_user)

@pytest.fixture
def function_file(files_client):
    """
    Фикстура для создания файла.

    :param files_client: Фикстура для инициализации клиента для работы с файлами (FilesClient)
    :return: Pydantic-модель, объединяющая запрос и ответ при создании файла.
    """
    request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)