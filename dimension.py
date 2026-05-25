# Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
# Input:
# Dimensions of the milk tank
# H = 20cm, L = 20cm, B = 20cm

# Dimensions of the glass
# h = 3cm, r = 1cm

# Tank dimensions
H = float(input("Enter tank height (cm): "))
L = float(input("Enter tank length (cm): "))
B = float(input("Enter tank breadth (cm): "))

# Glass dimensions
h = float(input("Enter glass height (cm): "))
r = float(input("Enter glass radius (cm): "))

# Volume of tank
tank_volume = H * L * B

# Volume of glass
pi = 3.14
glass_volume = pi * r * r * h

# Number of glasses
number_of_glasses = tank_volume / glass_volume

print("Number of glasses filled:", int(number_of_glasses))