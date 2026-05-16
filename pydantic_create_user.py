from pydantic import BaseModel, Field, EmailStr
from tools.fakers import Fakers


class CreateUserRequestSchema(BaseModel):
    """
    Схема для выполнения запроса на создание пользователя.
    """
    email: EmailStr = Field(default_factory=Fakers.get_random_email_for_user, min_length=1, max_length=250)
    password: str = Field(min_length=1, max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


class UserSchema(BaseModel):
    """
    Схема пользователя (полная информация).

    Используется для представления данных пользователя в ответах API,
    включая системный идентификатор.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа при успешном запросе на создание пользователя.
    """
    user: UserSchema
