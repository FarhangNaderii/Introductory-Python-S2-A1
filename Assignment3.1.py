import random

times_you_tried=0
pc_number=random.randint(1,20)

while True:
    guess=int(input("enter number :"))
    times_you_tried +=1
    if guess==pc_number:
        print("you won")
        print("you tried", times_you_tried ,"times")
        break
    else:
        if guess<pc_number:
            print("increase your number")
        else:
            print("decrease your number")
            continue

