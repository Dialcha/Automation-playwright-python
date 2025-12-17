class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.first_add_to_cart_btn = ".inventory_item button"
        self.cart_badge = ".shopping_cart_badge"
        self.cart_link = ".shopping_cart_link"

    def add_first_product_to_cart(self):
        self.page.locator(self.first_add_to_cart_btn).first.click()

    def get_cart_count(self):
        return self.page.locator(self.cart_badge).inner_text()

    def go_to_cart(self):
        self.page.click(self.cart_link)
