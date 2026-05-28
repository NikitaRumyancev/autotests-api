import pytest
from clients.files.files_client import get_private_file_client, FilesClient
from clients.files.file_schema import CreateFileRequestSchema, CreateFileResponseSchema
from pydantic import BaseModel

from fixtures.users import UserFixture


class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_private_file_client(user=function_user.authentication_user)

@pytest.fixture
def function_file(files_client):
    request = CreateFileRequestSchema(upload_file="./test_data/files/playwrite.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)