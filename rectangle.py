# 9. Write a program that calculates the perimeter and area of a rectangle,
# using the formulas P = 2(w + l) and A = wl, where w is the width and l is the length

# Ask the user for the Width and Length of the rectangle
width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the lenght of the rectangle: "))

# Calculate the perimeter
perimeter = 2 * (width + length)

# Calculate the are of a rectangle
area = width * length

# Display the results
print("Perimeter of the rectangle:",perimeter)
print("Area of the rectangle:",area)