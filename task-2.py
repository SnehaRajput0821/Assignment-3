# Program to perform calculations using the math module

import math

# Step 1: Ask the user for a number
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
sqrt_val = math.sqrt(num)          # Square root
log_val = math.log(num)            # Natural logarithm (base e)
sine_val = math.sin(num)           # Sine of the number (in radians)

# Step 3: Display the results
print("Square root of", num, "is:", sqrt_val)
print("Natural logarithm of", num, "is:", log_val)
print("Sine of", num, "is:", sine_val)