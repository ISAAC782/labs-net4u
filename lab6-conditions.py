from time import sleep
import math
print("Hello, choose one of the options bellow:")
print("Menu:\n")
print("1.insert number and ** bye 3")
print("2.Insert 4 IPs to a list and print it")
print("3.insert 4 entries to DNS_dictionary and print it")
print("4.check if a string is polindrom")

option=(input("my choise is:"))
if (option.isdigit() and int(option)<=4 and int(option)>=0):

    if(int(option)==1):
        number=int(input("insert your number :"))
        print ("The result is:"+ str(math.pow(number,3)))
    elif(int(option)==2):
        print("Enter 4 IPs:")
        ip_list=[]
        ip_list.append(input("IP number 1:"))
        ip_list.append(input("IP number 2:"))
        ip_list.append(input("IP number 3:"))
        ip_list.append(input("IP number 4:"))
        print("your ips are:"+str(ip_list))
    elif(int(option)==3):
        print("Enter 4 DNS:")
        DNS_list = {}
        DNS_list.update({input("DNS 1 key:"):input("DNS 1: value")})
        DNS_list.update({input("DNS 2 key:"):input("DNS 2: value")})
        DNS_list.update({input("DNS 3 key:"):input("DNS 3: value")})
        DNS_list.update({input("DNS 4 key:"):input("DNS 4: value")})
        print("Your DNS list is:"+str(DNS_list))
    elif (int(option) == 4):
        string=input("Enter string to check if polindrom:")
        if (string == string[::-1]):
            print("This is polindrom")
        else:
            print("This is not polindrom")


else:
    print("insert only numbers between 1-4!")

