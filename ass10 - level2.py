import unittest

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self, user_name):
        self.user_name = user_name
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def remove_from_cart(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return True
        return False

    def display_cart(self):
        return self.products


# Unit Test Class
class TestCart(unittest.TestCase):

    def setUp(self):
        """Runs before every test"""
        self.cart = Cart("Trupti")
        self.product1 = Product("Laptop", 60000, 1)
        self.product2 = Product("Mouse", 500, 2)

    def test_add_to_cart(self):
        """Test adding product to cart"""
        self.cart.add_to_cart(self.product1)
        self.assertEqual(len(self.cart.products), 1)
        self.assertEqual(self.cart.products[0].name, "Laptop")

    def test_remove_from_cart(self):
        """Test removing product from cart"""
        self.cart.add_to_cart(self.product1)
        self.cart.add_to_cart(self.product2)

        result = self.cart.remove_from_cart("Mouse")
        self.assertTrue(result)
        self.assertEqual(len(self.cart.products), 1)

    def test_remove_non_existing_product(self):
        """Test removing product not in cart"""
        self.cart.add_to_cart(self.product1)

        result = self.cart.remove_from_cart("Keyboard")
        self.assertFalse(result)
        self.assertEqual(len(self.cart.products), 1)

    def test_display_cart(self):
        """Test displaying cart contents"""
        self.cart.add_to_cart(self.product1)
        self.cart.add_to_cart(self.product2)

        products = self.cart.display_cart()
        self.assertEqual(len(products), 2)


# Run the tests
if __name__ == "__main__":
    unittest.main()