import pytest

@pytest.mark.ui
@pytest.mark.regression
def test_user_can_add_product_to_cart(page, login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_product_to_cart()
    cart_count = inventory_page.get_cart_count()

    assert cart_count == "1"
