def show():

    for row in game_board:
        for cell in row:
            print(cell,end="")
        print()


def check_player1():
    if game_board[0][0]=="x" and game_board[0][1]=="x" and game_board[0][2]:
        print("you win")
    if game_board[1][0]=="x" and game_board[1][1]=="x" and game_board[1][2]:
        print("you win")
    if game_board[2][0]=="x" and game_board[2][1]=="x" and game_board[2][2]:
        print("you win")
    if game_board[0][0]=="x" and game_board[1][0]=="x" and game_board[2][0]:
        print("you win")
    if game_board[0][1]=="x" and game_board[1][1]=="x" and game_board[2][1]:
        print("you win")
    if game_board[0][2]=="x" and game_board[1][2]=="x" and game_board[2][2]:
        print("you win")
    if game_board[0][0]=="x" and game_board[1][1]=="x" and game_board[2][2]:
        print("you win")
    if game_board[0][2]=="x" and game_board[1][1]=="x" and game_board[2][0]:
        print("you win")

def check_player2():
    if game_board[0][0]=="o" and game_board[0][1]=="o" and game_board[0][2]:
        print("you win")
    if game_board[1][0]=="o" and game_board[1][1]=="o" and game_board[1][2]:
        print("you win")
    if game_board[2][0]=="o" and game_board[2][1]=="o" and game_board[2][2]:
        print("you win")
    if game_board[0][0]=="o" and game_board[1][0]=="o" and game_board[2][0]:
        print("you win")
    if game_board[0][1]=="o" and game_board[1][1]=="o" and game_board[2][1]:
        print("you win")
    if game_board[0][2]=="o" and game_board[1][2]=="o" and game_board[2][2]:
        print("you win")
    if game_board[0][0]=="o" and game_board[1][1]=="o" and game_board[2][2]:
        print("you win")
    if game_board[0][2]=="o" and game_board[1][1]=="o" and game_board[2][0]:
        print("you win")


game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

for row in game_board:
    for cell in row:
        print(cell, end="")
    print()


while True:

    print("player 1 :")

    while True:
        row= int(input("Enter row :"))
        col= int(input("Enter col :"))
        if 0 <= row <=2 and 0 <= col <=2:

            if game_board [row][col]=="-":
                game_board[row][col]= "x"
                break
            else:
                print("please select another number")
        else:
            print("select number between 0 to 2")
    game_board[row][col] = "x"
# for row in game_board:
#     for cell in row:
#         print(cell,end="")
#     print()

    show()
    check_player1()

    print("player 2 :")

    while True:
        row= int(input("Enter row :"))
        col= int(input("Enter col :"))
        if 0 <= row <=2 and 0 <= col <=2:
            if game_board [row][col]=="-":
                game_board[row][col]= "o"
                break
            else:
                print("please select another number")
        else:
            print("select number between 0 to 2")
    game_board[row][col] = "o"
# for row in game_board:
#     for cell in row:
#         print(cell,end="")
#     print()
    show()
    check_player2()
