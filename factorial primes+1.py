import math
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
    return "prime"

q=1
a=int(input('stop at: '))
while q<=a:
    p=math.factorial(q)+1
    if is_prime_fermat(p)=="prime":
        print(f"{q}!+1 = {p} {is_prime_fermat(p)}")
    q+=2