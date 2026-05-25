# 15. Create a program that prompts the user for the radius of a sphere
# and calculates and displays its volume.

import math

# Prompt the user for the radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume of the sphere using the formula V = (4/3) * π * r³
volume = (4/3) * math.pi * radius ** 3

# Display the result
print("The volume of the sphere is:",volume)