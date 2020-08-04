'''#simple examples of lists commands:
new_list=[1,2,3,4]   #define list
new_list2=list("1234f") #define lists using string
print(new_list2)
new_list3=''.join(new_list2) #unite the cells to one string
print(new_list3)

string="Hi how are you\n I'm fine..."
list4=string.split() #seperate according words
print(list4)
list4=string.splitlines() #seperate according lines
print(list4)

my_list=["hello",1,66.6,"yossi"]
print ("The length is: " +str(len(my_list))) # print the length of the list

my_list2= "11324123rfdfbdfbdsb"
print ("The length is: " +str(len(my_list2)))
my_list3=[2,34,"erere",52,"er"]
my_list3.append("HI") #how to add cell to the list
print (my_list3)
my_list3.insert(3,"daay") #how to insert cell in specific place
print (my_list3)

my_list3.pop(3) # remove cell number 3
print (my_list3)'''

# Dictionary simple example commands
#definition
dict1={}
print(dict1)
dict1={"noam":24,"david":25}
print(dict1)
#adding dictionaries
dict2={"aviv":21,"dina":24}
print(dict2)
dict3={}
dict3.update(dict1)
dict3.update(dict2)
print(dict3)
print(len(dict3))
print(dict3["aviv"])
print(dict3.values())   #print dict values
dict3["noam"]=26        #update value of specific cell
print(dict3)
print("noam" in dict3)    #print true if the key exists in the dictionary.
print(26 in dict3.values()) # print true if the value exists in the dictionary
