import math

def function(a,b,c):
    delta=(b*b)-(4*a*c)
    if delta < 0:
        print("this function has no true answer.")
    elif delta==0:
        a1=-b / (2*a)
        print("function 1 has true answer :",a1)
    else:
        a1=(-b - math.sqrt(delta)) / (2*a)
        a2=(-b + math.sqrt(delta)) / (2*a)
        print("second function has true answer, answers are :", a1, ",", a2)

a , b , c=input("enter a , b , c :").split(",",2)
a , b , c=int(a),int(b),int(c)

print("\n")

function(a,b,c)
