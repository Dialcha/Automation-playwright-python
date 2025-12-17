import pytest

@pytest.mark.api
@pytest.mark.regression
def test_create_user(reqres_client):
    response = reqres_client.create_user("Diego", "QA Lead")
    assert response.status_code == 201
    assert response.json()["name"] == "Diego"
