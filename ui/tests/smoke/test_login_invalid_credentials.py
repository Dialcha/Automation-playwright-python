import pytest

@pytest.mark.ui
@pytest.mark.smoke
def test_login_with_invalid_credentials_shows_error(page, login_page):
    login_page.login("invalid_user", "wrong_password")

    error_message = page.locator("[data-test='error']").inner_text()
    assert "Username and password do not match" in error_message
