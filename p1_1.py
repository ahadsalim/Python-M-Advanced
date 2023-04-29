import math

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# Function to count the number of prime divisors of a number
def count_prime_divisors(n):
    count = 0
    for i in range(2, n+1):
        if is_prime(i) and n % i == 0:
            count += 1
    return count

# Read the 10 numbers from input
numbers = []
for i in range(10):
    n = int(input("Enter a number: "))
    numbers.append(n)

# Find the number with the highest number of prime divisors
max_divisors = 0
max_number = 0
for n in numbers:
    divisors = count_prime_divisors(n)
    if divisors > max_divisors:
        max_divisors = divisors
        max_number = n
    elif divisors == max_divisors and n > max_number:
        max_number = n

# Print the result
print("The number with the highest number of prime divisors is", max_number)
print("It has", max_divisors, "prime divisors.")
