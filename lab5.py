#lab 5 - dictionary exercise

money_dict={"avi":20000,"idan":40000,"yossi":10000,"avigdor":25000,"ihia":80000}
print("The first man and the last man in the entry has "+str(money_dict["avi"]+money_dict["ihia"]) + " shekels.")
money_dict["dudu"]=money_dict["avi"]+money_dict["ihia"]
print("the length of the entry is: "+str(len(money_dict)))
print("idan" in money_dict)