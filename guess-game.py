import random
b = random.randint(1,20)
correct=True

while correct:
    a = int(input("Guess a number between 1 and 20: "))
    if a==b:
        print("Yeyy! You guessed the number right")
        correct=False
