import pytest
from api.clients.reqres_client import ReqResClient

@pytest.fixture
def reqres_client():
    return ReqResClient("https://reqres.in/api")
