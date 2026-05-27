import pytest
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client

@pytest.fixture
def authentication_client() -> AuthenticationClient:
    """
    Фистура, которая создаем готовый http Client.

    :return: AuthenticationClient
    """
    return get_authentication_client()