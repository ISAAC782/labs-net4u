my_details=["eliran yahav",35,"eliran@gmail.com","0544336774"]
print("my name is: "+my_details[0]+"\nI am "+str(my_details[1])+" years old"+"\nmy mail is: "+my_details[2]+"\nMy phone number is :"+ my_details[3])
ip_list=["192.168.1.1","192.168.1.2"]
ip_list.append("192.168.1.3")
ip_list.append("192.168.1.4")
ip_list.append("192.168.1.5")
ip_list.pop(3)
print("we have "+str(len(ip_list))+" IP addresses"+"\nThe adresses are:"+str(ip_list))