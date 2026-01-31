# List to store registered products
product_database = []

class Product:
    # Constructor to initialize product details
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Method to display product information
    def display_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


# Function to register a product
def register_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    # Create Product object
    new_product = Product(name, price, quantity)

    # Store product in database
    product_database.append(new_product)

    print("\nProduct registered successfully!\n")


# Register a product
register_product()

# Display all registered products
print("Registered Products:")
for product in product_database:
    product.display_info()
    print()
