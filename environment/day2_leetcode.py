# LeetCode #412 — FizzBuzz
# For numbers 1 to n:
#   Divisible by 3 AND 5 → "FizzBuzz"
#   Divisible by 3 only  → "Fizz"
#   Divisible by 5 only  → "Buzz"
#   Otherwise            → the number as a string

def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print(fizzBuzz(15))