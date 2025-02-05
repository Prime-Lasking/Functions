def sigma(n):
    x=0
    for i in range(1, n+1):
        if n%i==0:
            x+=i
    return x
print(sigma(int(input('what number do you want to put in? '))))