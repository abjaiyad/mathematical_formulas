# 8. Write a program that calculates the delta of a quadratic equation (Δ = b² - 4ac).

# Prompt the user for coefficients of the quadratic equation
a = float(input("Enter the coefficients a: "))
b = float(input("Enter the coefficients b: "))
c = float(input("Enter the coefficients c: "))

# Calculate the delta
delta = b**2 - 4*a*c

# Display the result
print("The delta (Δ) of the quadratic equation is:", delta)