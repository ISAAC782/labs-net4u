filepath="C:/Users/elira/OneDrive/Desktop/file.txt"

file=open(filepath,"r+")
file.write("Hello")
file.close()

file=open(filepath,"r")
print(file.read())
file.close()