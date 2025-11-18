def factorial(number):
    if number <= 2:
        return number
    return factorial(number - 1) * number

print(factorial(5))