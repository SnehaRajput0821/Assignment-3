# Program to calculate factorial using a loop

def factorial(n):
    result = 1
    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result

# Sample call
num = 5
print("Factorial of", num, "is:", factorial(num))