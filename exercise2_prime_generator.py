try:
    # Take range inputs from user
    start = int(input("Enter range start: "))
    end = int(input("Enter range end: "))

    # Validate positive integers
    if start <= 0 or end <= 0:
        raise ValueError("Numbers must be positive.")

    # Function to check prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Find primes
    primes = [num for num in range(start, end + 1) if is_prime(num)]

    # Display 10 numbers per line
    print("Prime numbers:")
    for i in range(0, len(primes), 10):
        print(" ".join(map(str, primes[i:i+10])))

except ValueError as ve:
    print("Input Error:", ve)
except Exception as e:
    print("Unexpected Error:", e)
