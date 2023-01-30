import random
print("GUESS THE NUMBER \n")
lowerlimit=int(input("Enter lower limit: ")) 
upperlimit=int(input("Enter upper limit: ")) 
rand=random.randrange(lowerlimit, upperlimit)
a=0
c=1
while a<=c:
    num=int(input("Guess a number:"))
    c=c+1
    if rand==num:
        print("you have won!")
    else:
        print("try again")
