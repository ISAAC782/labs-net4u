#This program calculates the price of some prodact in the market.
#The price of tomatos: 3 NIS per kg
#The price of cucamber 2 NIS per kg
#The price of cola 5 NIS
#The price of chicken 20 NIS per kg
print("Hello,\nThis is pur prices\nTomatoes-3 NIS per kg\n"+"cucamber-2 NIS per kg\n"+"cola-5 NIS per bottle\n"+"chicken-20kg per kg\n")

tomatoes_p=int(input ("Enter the amount of tomatoes you want in kg:"))*3
cucambers_p=int(input ("Enter the amount cucambers you want in kg:"))*2
cola_p=int(input ("Enter the amount cola bottles you want"))*5
chicken_p=int(input("Enter the amount of chicken you want in kg"))*20
price=tomatoes_p+cucambers_p+cola_p+chicken_p
print("\nYour bill is:\n"+ "Tomatoes:     "+str(tomatoes_p)+" NIS\n"+"Cucambers:    "+str(cucambers_p)+"NIS\n"+"cola:        "+str(cola_p)+"NIS\n"+"chicken:     "+str(chicken_p)+"NIS\n")
print("\nYour total price:\n"+str(price)+"  shekels")
print("\nPrice include MAAM:"+ str("%.2f" % (price*1.17)) +" NIS")