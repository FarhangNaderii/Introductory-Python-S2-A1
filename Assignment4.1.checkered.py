def checkered_board(n,m):
    for row in range(n):
        str=""
        for col in range(m):
            if row %2 ==0:
                str += "*#"
            else:
                str += "#*"
        print(str)

n , m= input("enter n and m one after another :").split(",",1)
n , m= int(n),int(m)

print("\n")
checkered_board(n,m)
