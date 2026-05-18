from pydantic import BaseModel, ConfigDict, Field


class TokenSchema(BaseModel):
    """
    Структура аутентификационных токенов.
    """
    model_config = ConfigDict(populate_by_name=True)
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):
    """
    Структура ответа от сервера при успешной аутентификации.
    """
    token: TokenSchema


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    model_config = ConfigDict(populate_by_name=True)
    refresh_token: str = Field(alias="refreshToken")
