import pytest

@pytest.mark.ui
@pytest.mark.smoke
def test_user_can_login(page, login_page):
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in page.url
