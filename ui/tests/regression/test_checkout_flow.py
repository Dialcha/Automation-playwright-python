import pytest

@pytest.mark.ui
@pytest.mark.regression
def test_user_can_start_checkout(page, login_page, inventory_page, cart_page):
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_product_to_cart()
    inventory_page.go_to_cart()

    cart_page.start_checkout()

    assert "checkout-step-one" in page.url
