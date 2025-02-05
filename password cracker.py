import time
from random import *

guess = ""
password = input("Password: ")
letters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
start_time = time.time()
while guess != password:
    guess = ""
    for letter in password:
        guessletter = letters[randint(0, 9)]
        guess = str(guessletter) + str(guess)
    print(guess)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Password guessed in {elapsed_time:.10f} seconds!")
input("")
