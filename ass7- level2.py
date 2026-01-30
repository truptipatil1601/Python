# List to act as user database
user_database = []

class User:
    # Constructor to initialize user details
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # Method to display user information
    def display_info(self):
        print("Name:", self.name)
        print("Email:", self.email)


# Function to validate email format
def is_valid_email(email):
    return "@" in email and "." in email


# Function to check email uniqueness
def is_unique_email(email):
    for user in user_database:
        if user.email == email:
            return False
    return True


# User registration function
def register_user():
    name = input("Enter name: ")
    
    while True:
        email = input("Enter email: ")
        if not is_valid_email(email):
            print("Invalid email format. Try again.")
        elif not is_unique_email(email):
            print("Email already registered. Try another.")
        else:
            break

    password = input("Enter password: ")

    # Create User object
    new_user = User(name, email, password)

    # Store in database
    user_database.append(new_user)

    print("\nUser registered successfully!\n")


# Register users
register_user()

# Display all registered users
print("Registered Users:")
for user in user_database:
    user.display_info()
    print()
