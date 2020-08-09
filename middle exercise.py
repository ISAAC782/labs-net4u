# this program is all the middle exercises together:
import time
import math
from datetime import date
def addkey(d1,key,value):
    d2={key:value}
    d1.update(d2)
    return d1

while True:
    option=input("Choose exercise to see:  ( type 1-14 or q for quit...)\n")
    if(option == "q"):
        break
    if (option.isdigit() and int(option)<=14 and int(option)>=0):
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
            if (int(option) == 8):
                n=20
                d={"x":20}
                n=type(n)()
                d=type(d)()
                print("The variables are empty now:\n" +str(n)+str(d))
            if (int(option) == 9):
                dict={"key1":1,"key2":2}
                print("before update:"+str(dict))
                dict2=addkey(dict,"key3",3)
                time.sleep(1)
                print("after update:" + str(dict2))
            if (int(option) == 10):
                ls={}
                ls=list("net4u")
                net_dict={}
                for i in range(len(ls)):
                    net_dict.update({ls[i]:1})
                print(net_dict)
            if (int(option) == 11):
                str1=input("Enter first str")
                str2=input("Enter second str")
                str=str2[:2:]+str1[2::]+" "+str1[:2:]+str2[2::]
                print ("The new string is:"+ str )
            if (int(option) == 12):
                string=input("enter your string")
                dict_count={} #empty dictionary to contain each letter in the string and the numer of times it apears
                for letter in string:  #run through the letters on the string
                    if letter in dict_count: #if the letter is already exist in the dictionary add 1
                        dict_count[letter]+=1
                    else:
                        dict_count[letter]=1 #if the letter is not exist create ney key for this letter and set value to 1
                for key in dict_count:
                    print("letter "+key+" apears "+str(dict_count[key])+" times.")
            if (int(option) == 13):
                list=[1,4,5,3,6,3413,545,3]
                sum=0
                for i in range(len(list)):
                    sum=sum+int(list[i])
                print ("sum of list is: "+str(sum))
            if (int(option) == 14):
                cells_to_remove=[0,4,5]
                list1=["green","yellow","white","red","blue","black"]
                print("The list before update is:\n" +str(list1))
                for i in range(len(cells_to_remove)):

                    del list1[cells_to_remove[i]]
                    j=i
                    for j in range(len(cells_to_remove)):
                            cells_to_remove[j]-=1

                print("The list before update is:\n" + str(list1))

    else:
            print("please enter numbers between 1-13")