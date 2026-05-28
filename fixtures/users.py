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
    def user_id(self):
        """
        Геттер для user_id.

        :return: str.
        """
        return self.response.user.id

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        """
        Геттер для email и password.

        :return: Pydantic-модель, которая в себе содержит поля email, password.
        """
        return AuthenticationUserSchema(email=self.email,
                                        password=self.password)

@pytest.fixture
def public_user_client() -> PublicUsersClient:
    """
    Фистура для инициализации клиента без авторизации для работы с пользователями.

    :return: Настроенный клиент для работы с пользователями (PublicUsersClient).
    """
    return get_public_user_client()

@pytest.fixture
def private_user_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Фикстура для инициализации клиента с авторизацией для работы с пользователями.

    :param function_user: Фикстура с данными созданного пользователя
    :return: Настроенный клиент для работы с пользователями (PrivateUsersClient).
    """
    return get_private_user_client(user=function_user.authentication_user)

@pytest.fixture
def function_user(public_user_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура для создания пользователя.

    :param public_user_client: Фикстура для инициализации клиента для работы с пользователями (PublicUsersClient).
    :return: Модель для агрегации возвращаемых данных фикстурой function_user
    """
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request=request)
    return UserFixture(request=request, response=response)