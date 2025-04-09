
n = int(input("Choose your number"))

import random


def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    def miller_rabin_test(d, n):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(1, len(bin(n)) - 2):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        if not miller_rabin_test(d, n):
            return "it's not prime"
    return "it's prime"


print(is_prime_miller_rabin(n))
