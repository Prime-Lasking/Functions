#The fastest primality program
import time
import random
def is_prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return "it's not prime"
    return "it's prime"

start_time = time.time()
result = is_prime_fermat(n)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"{result} found in {elapsed_time:.6f} seconds")