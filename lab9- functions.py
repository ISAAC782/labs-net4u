
def menu():
        print("menu:\nchoose one of this options:")
        print("1.Dogs details.\n2.freinds list\n3.N azeret\n")
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
    print (new in name)
def azeret():
    num=int(input("Enter your number: "))
    for i in range(num-1,1,-1):
        num=num*i
    print("The result is: "+ str(num))

###################### main ###################
option=int(menu())
if(option==1):
    dogs_details()
elif(option==2):
    name_list =freind_list()
    check_freind(name_list)
elif(option==3):
    azeret()