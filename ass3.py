num1 = 8
num2 = 3

print(f"Let's suppose the first number: {num1} and the second number: {num2}")

# 1. Sum
sum_result = num1 + num2
print(f"1. Sum of the two numbers: {sum_result}")

# 2. Subtraction
sub_result = num1 - num2
print(f"2. Result of subtraction: {sub_result}")

# 3. Product
product_result = num1 * num2
print(f"3. Product of the two numbers: {product_result}")

# 4. Division (with error handling)
if num2 != 0:
    division_result = num1 / num2
    print(f"4. Quotient of division: {division_result}")
else:
    print("4. Quotient of division: Cannot divide by zero")

    