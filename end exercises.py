from datetime import date
import math
def exercise1():
    print('''Twinkle, twinkle, little star,
            How I wonder what you are!
                 Up above the world so high,
                 Like a diamond in the sky.
            Twinkle, twinkle, little star,
                 How I wonder what you are''')
def exercise2():
    color_list=["red","green","white","black"]
    print("the first cell is:" +str(color_list[0]))
    print("the last cell is:" +str(color_list[(len(color_list))-1]))

def exercise3():
    n=int(input("enter integer number"))
    result= n+n*n+n*n*n
    print ("The result is: "+ str(result))
def exerxise4():
    date1 = date(2014, 7, 2)
    date2 = date(2014, 9, 11)
    delta = date2 - date1
    print(delta.days)
def exercise5():
    num=[]
    eq=True
    sum=0
    for i in range (0,3):
        num.append(int(input("enter your "+ str(i) +" number")))
        sum=sum+num[i]
    for i in range (0,2):
        if (num[i]!=num[i+1]):
            eq= False
            print ("The numbers are different. The sum is: "+str(sum))
            break
        else:
            continue
    if eq==True:
        print ("the numbers are equal, the three time of sum is : "+ str(int(sum)*3))

def exercise6():
    num1=int(input("enter first num"))
    num2 = int(input("enter second num"))
    sum=num1+num2
    if (sum <20 and sum >15):
        sum=20
        print ("the value is 20")
    else:
        print("The value is: "+ str (sum))
def exercise7():
    print("my name is Eliran\nI am 35 years old\nMy address is North")
def exercise8():
    num1=int(input("enter first num"))
    num2 = int(input("enter second num"))
    sum=math.pow(num1+num2,2)
    print("The result is : " + str(sum))
def exercise9():
    unit = input("do you wand to convert height in feets or inches? (1 for feets,2 for inches)")
    height = float(input("Enter your height please..."))
    if (int(unit) == 1):
        print("your height in centimeters is: " + str(height * 30.48))
    else:
        print("your height in centimeters is: " + str(height * 2.54))

def exercise10():
    num=int(input("Enter num"))
    sum=0
    for i in range(1,num):
        print (i)
        sum=sum +i*i
    print("The sum of cubes is: "+str(sum))
while True:
    option=input("Choose exercise to see:  ( type 1-14 or q for quit...)\n")
    if(option == "q"):
        break
    if (option.isdigit() and int(option)<=14 and int(option)>=0):
        if int(option) == 1:
            exercise1()
        elif int(option) == 2:
            exercise2()
        elif int(option) == 3:
            exercise3()
        elif int(option) == 4:
            exerxise4()
        elif int(option) == 5:
            exercise5()
        elif int(option) == 6:
            exercise6()
        elif int(option) == 7:
            exercise7()
        elif int(option) == 8:
            exercise8()
        elif int(option) == 9:
            exercise9()
        elif int(option) == 10:
            exercise10()