def fibonacci(n):
    array=[]
    f1=0
    f2=1
    for i in range(n):
        if i==0:
            array.append(f2)
        else:
            array.append(f2+f1)
            f1=f2
            f2= array[i]
    array = array[::-1]
    string = ""
    for i in range(n):
        if i==0:
            string += str(array[i])
        else:
            string += ","+str(array[i])
    print(string)
    
n=int(input("enter n :"))
fibonacci(n)
