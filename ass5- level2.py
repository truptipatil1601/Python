# Open the file in read mode
file = open("data.txt", "r")

# Read all lines and count them
line_count = len(file.readlines())

# Close the file
file.close()

# Display the result
print("Number of lines in the file:", line_count)
