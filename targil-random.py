from random import randint
import time
loto_numbers=[[0,0,0,0,0,0,0],[]]
for i in range(1000):
    for j in range(7):
        if(j<6):
            loto_numbers[j]=randint(1,37)
        elif(j==6):
            loto_numbers[j] = randint(1,7)
    print("The numbers are:"+str(loto_numbers))


