import random

# List of syllables
syllables = [
    "ka", "lo", "mi", "ra", "ta", "ne", "shi", "zo",
    "fi", "da", "ru", "va", "ki", "mo", "sa"
]

# Ask user for number of names
n = int(input("Enter number of character names to generate: "))

# Set to store unique names
names = set()

# Generate unique character names
while len(names) < n:
    name = random.choice(syllables) + random.choice(syllables) + random.choice(syllables)
    names.add(name.capitalize())

# Save names to file
with open("character_names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("Character names generated and saved to character_names.txt")
