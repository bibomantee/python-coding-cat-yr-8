
#Task 6

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 11):
    print(fibonacci(i), end=", ")

print(fibonacci(10))