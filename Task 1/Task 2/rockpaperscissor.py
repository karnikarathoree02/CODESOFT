import random

("0=rock")
("1=paper")
("2=scissor")
S= int(input("Enter your choice:"))

num=random.randint(0,3)
if(S==num):
    print("Game Draw")
elif(S==0 & num==2 | S==1 &num==0 |S==2 & num==1):
    print("You win")
else:
    print("Computer win")
if (num==0):
    print("Computer choose rock")
elif(num==1):
    print("Computer choose paper")
elif(num==2):
    print("Computer choose scissor")
else:                    
    print("Default")
