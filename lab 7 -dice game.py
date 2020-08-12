from random import randint
import time

def check_profit(dice1,dice2):
    if (dice1==dice2 and dice1==6):
        print("6X6!!! you won 1000 shekels!!!!!")
        money=1000
    elif (dice1==dice2):
        print("double ! you won 100 shekels!!!!!")
        money = 100
    elif (dice2==2):
        print("dice 2 equal 2! you won 40 shekels!!!!!")
        money = 40
    elif (dice1==1):
        print("you won 20 shekels!!!!!")
        money = 20
    else:
        print("sorry, you didn't win.... maybe next time...")
        money = -3
    return money

my_money=int(input("Enter the amount of money you have:\n"))
print("you have "+str(my_money) +" shekels")

while True:
    play=input("Do you want to play? cost is 3 shekels..\n press y or n\n")
    if (play=="y"):
        dice1=randint(1,6)
        dice2=randint(1,6)
        print ("your result is:")
        time.sleep(1)
        print(str(dice1)+","+str(dice2))
        my_money=my_money+int(check_profit(dice1,dice2))
        print("_________________________________")
        print("you money now is "+str(my_money))
        print("_________________________________")
        print("\n\n\n")
    if(play=="n"):
        print("Bye Bye... your money is:"+str(my_money))
        break

