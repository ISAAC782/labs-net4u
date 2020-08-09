# this program is all the middle exercises together:
import time
import math
from datetime import date
while True:
    option=input("Choose exercise to see:  ( type 1-13 or q for quit...)\n")
    if(option == "q"):
        break
    if (option.isdigit() and int(option)<=13 and int(option)>=0):
            if(int(option)==1):
                print("net4U, is the best place\n     ...in the world" )
            if (int(option) == 2):
                print(str(date.today())+"  "+str(time.strftime("%H.%M.%S")))
            if (int(option) == 3):
                name=input("Enter your name:")
                last_name=input("Enter your last name")
                print("your name and your last nemr in reverse are:\n"+name[::-1]+" "+last_name[::-1])
            if (int(option) == 4):
                file_name=input("enter your file name:\n")
                if("." in file_name):
                    print("your extended is "+file_name[file_name.find(".")::])
                else:
                    print("sorry' bad file name")
            if (int(option) == 5):
                n=int(input("enter you number please: "))
                print ("The result is: "+str(n+math.pow(n,2)+math.pow(n,3)))
            if (int(option) == 6):
                num=int(input("Enter your number please..."))
                if(num%2==0):
                    print("your number is even")
                else:
                    print("your number is odd")
            if (int(option) == 7):
                unit=input("do you wand to convert height in feets or inches? (1 for feets,2 for inches)")
                height = float(input("Enter your height please..."))
                if(int(unit)==1):
                    print ("your height in centimeters is: " + str(height*30.48) )
                else:
                    print("your height in centimeters is: " + str(height *2.54))

    else:
            print("please enter numbers between 1-13")