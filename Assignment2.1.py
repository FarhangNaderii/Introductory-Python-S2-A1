import math
while True:
    num1 = float(input("enter num1 :"))
    op = input("enter your intended mathematical marks from(+ , -, *, /, radical, sin, cos, tan, cot,factorial, exit) :")
    if op=="sin":
        answer = (math.sin(math.radians(num1)))
    if op=="cos":
        answer = (math.cos(math.radians(num1)))
    if op=="radical":
        answer = math.sqrt(num1)
    if op=="tan":
        answer = (math.tan(math radians(num1)))
    if op=="cot":
        answer = (1/(math.tan(math.radians(num1))))
    if op=="factorial":
        num1 = math.floor(num1)
        answer = math.factorial(num1)
    if op=="+":
        num2=float(input("enter number2 :"))
        answer=num1+num2
    if op=="-":
        num2=float(input("enter number2 :"))
        answer=num1-num2
    if op=="*":
        num2=float(input("enter number2 :"))
        answer=num1*num2
    if op=="/":
        num2=float(input("enter number2 :"))
        if num2==0:
            answer= "error"
        else:
            answer= num1/num2
    if op=="end":
        break
    print("answer :",answer)
        