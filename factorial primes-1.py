import math
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
    return "prime"

q=3
a=int(input("up to: "))
while q<=a:
    p=math.factorial(q)-1
    if is_prime_miller_rabin(p)=="prime":
        print(f"{q}!-1 is {is_prime_miller_rabin(p)}")
    q+=2