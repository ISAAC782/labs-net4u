
#this program get an input of numbrt and shows the number of thousends, hundreds ,dozend and units.
number=int(input ("Hi \nplease enter your number:\n"))
Alafim=(number)//1000
meot=(number%1000)//100
Asarot=(number%100)//10
Ahadot=(number%10)
print("Alafim= "+ str(Alafim)+"\n")
print("Meot= "+ str(meot)+"\n")
print("Asarot= "+ str(Asarot)+"\n")
print("Ahadot= "+ str(Ahadot)+"\n")
#all the calculation in one line if we care about efficiency:
print ("alafim=" + str(number//1000)+ "\n" +"meot="+str(number%1000//100)+"\n"+"asarot="+str(number%100//10)+"\n"+"ahadot=" +str(number%10))