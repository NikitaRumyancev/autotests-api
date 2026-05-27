import pytest
from pydantic import BaseModel, EmailStr
from clients.users.public_users_client import PublicUsersClient, get_public_user_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.users.private_user_client import AuthenticationUserSchema
from clients.users.private_user_client import PrivateUsersClient, get_private_user_client


class UserFixture(BaseModel):
    """
    Модель для агрегации возвращаемых данных фикстурой function_user
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        """
        Геттер для email.

        :return: EmailStr.
        """
        return self.request.email

    @property
    def password(self) -> str:
        """
        Геттер для password.

        :return: str.
        """
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email,
                                        password=self.password)

@pytest.fixture
def public_user_client() -> PublicUsersClient:
    """
    Фистура, которая создаем готовый http Client.

    :return: PublicUsersClient.
    """
    return get_public_user_client()

@pytest.fixture
def private_user_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Фикстура для инициализации PrivateUsersClient.

    :param function_user: Фикстура с данными созданного пользователя
    :yield: Настроенный http клиент. Объект PrivateUsersClient.
    """
    return get_private_user_client(user=function_user.authentication_user)

@pytest.fixture
def function_user(public_user_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура для создания пользователя.

    :param public_user_client:
    :return:
    """
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request=request)
    return UserFixture(request=request, response=response)