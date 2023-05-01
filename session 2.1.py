side1 = int(input("enter your first intended number : "))
side2 = int(input("enter your second intended number : "))
side3 = int(input("enter your third intended number : "))
if side1<side2+side3 and side2<side1+side3 and side3<side1+side2 :
    print("your input numbers can be used to form a triangle")
else :
    print("your input numbers not suitable to form a triangle")
