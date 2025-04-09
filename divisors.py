num = int(input("choose your number"))


factor1 = 3
while (num % factor1):
        if (factor1 <= num):
            factor1 += 2

factor2 = num // factor1
print(factor2,factor1)

