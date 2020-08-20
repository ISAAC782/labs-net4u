from time import *
def menu():
    while True:

        choise1=input("Menu:\na.IP system?\nb.DNS system?")
        if choise1=="a":
            choise2=input("Menu:\n ____________\na.search for ip address from a list\nb.add IP address to a list\nc.Delete IP address from a list\nd.Print all the IPs to the screen\n")
            if choise2=="a":
                search_ip()
            if choise2=="b":
                add_ip()
            if choise2 == "c":
                delete_ip()
            if choise2=="d":
                print_ip()
        elif choise1=="b":
            choise2 = input("Menu:\n ____________\na.search for URL in a dictionary\nb.Add URL to a dictionary\nc.Delete Url from a dictionary\nd. Update IP address of specific URL\ne.print all URL and IPs\n")
            dict=create_URL_dictionary()
            if choise2=="a":
                search_URL(dict)
            if choise2=="b":
                add_URL(dict)
            if choise2 == "c":
                delete_URL(dict)
            if choise2=="d":
                update_IP_URL(dict)
            if choise2=="e":
                print_URL(dict)
        else:
            print ("Enter a or b only!")
########################################################ip functions ############################################
def search_ip():
    ip=input("Enter IP to serch...")
    filepath="C:/Users/elira/PycharmProjects/labs-net4u/IP_list.txt"
    file=open(filepath,"r")
    find=False
    print("searching IP....")
    sleep(1)
    i=0
    for line in file:
        i+=1
        if ip in line:
            print("This IP exists in line "+str(i))
            find=True
    if find==False:
        print(" This IP not exists...")
    file.close()
    return find
def add_ip():
    ip=input("Enter IP to add")
    filepath = "C:/Users/elira/PycharmProjects/labs-net4u/IP_list.txt"
    file = open(filepath, "a+")
    file.write(ip)
    file.close()
def print_ip():
    filepath = "C:/Users/elira/PycharmProjects/labs-net4u/IP_list.txt"
    file = open(filepath, "r")
    print(file.read())
    file.close()
def delete_ip():
    ip=input("Enter IP to delete")
    filepath = "C:/Users/elira/PycharmProjects/labs-net4u/IP_list.txt"
    file = open(filepath, "r+")
    with open(filepath, "r") as f:
        lines = f.readlines()
        sleep(3)
    with open(filepath, "w") as f:
        for line in lines:
            if line.strip("\n") != ip:
                f.write(line)
#################################### URL functions ##########################################################
def create_URL_dictionary():
    URL_dict={"www.google.com":"8.8.8.8","www.walla.co.il":"1.1.1.1","www.facebook.com":"2.2.2.2"}
    return URL_dict


def search_URL(dict):
    URL_IP =input ("Enter URL or IP to search...")
    if URL_IP in dict:
        print ("URL exists")
        for key,value in dict.items():
            if URL_IP == key:
                print("The IP is "+ value)

    elif URL_IP in dict.values():
        print("ip exists ")
        for key, value in dict.items():
            if URL_IP == value:
                print("The URL is " + key)
    else:
        print ("URL or IP don't exist")

def add_URL(dict):
    URL=input("enter URL to update...\n")
    ip = input("enter ip to update...\n")
    if URL not in dict and ip not in dict:
        dict.update({URL:ip})
    else:
        choise=input(" URL or ip is already exists. Do you want to update? y/n")
        if choise=="y":
            dict.update({URL: ip})
            print(dict)
        else:
            print("no changes has been made")
    print(dict)
def delete_URL(dict):
    print(dict)
    URL= input("enter to delete...")
    if URL in dict:
        del dict[URL]
        print(dict)
    else:
        print (URL +" is not exist in list. Nothing changed...")
def update_IP_URL(dict):
    URL = input("enter URL to update...\n")
    ip = input("enter ip to update...\n")
    if URL in dict or ip in dict:
        dict.update({URL: ip})
        print(dict)
    else:
        choise = input(" URL and ip is not  exists. Do you want to add ths url? y/n")
        if choise=="y":
            dict.update({URL: ip})
            print (dict)
        else:
            print ("no change has been made")
def print_URL(dict):
    print ("The dictionary is: "+ str(dict))