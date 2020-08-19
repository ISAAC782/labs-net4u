
def check_fib_list(list):
    fib=True
    i=0
    while (i+2)<len(list):
        if(list[i+2]!=list[i+1]+list[i]):
            fib=False
            break
        i+=1
    print(fib)
list1=[1,2,3,5,8,13,21,34]
list2=[2,5,6,4,2,7,2,5]

check_fib_list(list1)
check_fib_list(list2)
