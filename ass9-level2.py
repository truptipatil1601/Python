# Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# Cart class
class Cart:
    def __init__(self, user_name):
        self.user_name = user_name
        self.products = []   # list to store Product objects

    # Method to add product to cart
    def add_to_cart(self, product):
        self.products.append(product)
        print(f"{product.name} added to cart.")

    # Method to remove product from cart by name
    def remove_from_cart(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product_name} removed from cart.")
                return
        print("Product not found in cart.")

    # Method to display cart contents
    def display_cart(self):
        if not self.products:
            print("Cart is empty.")
            return

        print(f"\nShopping Cart of {self.user_name}:")
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
