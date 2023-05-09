import random

index=0
array=[]
a= int(input("how many characters do you want to put in a line? :"))
while True:
    if index != a:
        number=random.randint(1,500)
        if index==0:
            array.append(number)
            index +=1
        else:
            for i in range(len(array)):
                if number !=array[i]:
                    if i ==len(array)-1:
                        array.append(number)
                        index +=1
                    else:
                        continue
                else:
                    continue
    else:
        break
print(array)