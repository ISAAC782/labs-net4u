
def menu():
        print("menu:\nchoose one of this options:")
        print("1.Dogs details.\n2.freinds list\n3.N azeret\n4.exit")
        option=input()
        return option
def dogs_details():
    name=input("enter you dog name: ")
    age=input("enter your dog age: ")
    print("your dog name is: "+name+"\nyour dog human age is: "+str(int(age)*7) )
def freind_list():
    name=[]
    for i in range(0,5) :
        name.append(input("Enter name of your freind: "))
    print("your freind list is:"+ str(name))
    return(name)
def check_freind(name):
    new=input("enter new name friend: ")
    if (new in name):
        print("freind exist")
    else:
        print("freind is not exist")
def azeret():
    num=int(input("Enter your number: "))
    for i in range(num-1,1,-1):
        num=num*i
    print("The result is: "+ str(num))

###################### main ###################
while True:
    option=int(menu())
    if(option==1):
        dogs_details()
    elif(option==2):
        name_list =freind_list()
        check_freind(name_list)
    elif(option==3):
        azeret()
    elif (option == 4):
        print ("bye...")
        break
    else:
        print("Enter 1-3 only...")
