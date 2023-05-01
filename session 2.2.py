name = input("enter your name : ")
family = input("enter family : ")
score1= float(input("enter your first score : "))
score2 = float(input("enter your second score : "))
score3 = float(input("enter your third score : "))
average = (score1 + score2 + score3) / 3
print(average)
if average>=17: 
    print("congratulation your average is Great")
if 17>average>=12:
    print("Not bad your average is Normal")
if average<12:
    print("Work harder you were Failed")

