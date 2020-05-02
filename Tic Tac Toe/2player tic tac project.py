#tic tac toe game
import os
import sys
game=[" "," "," "," "," "," "," "," "," "]

def begin():
    n=2
    print("press\n 1) player1='x' and player2='0'\n 2) player1='0' and player2='X'")
    tr=int(input())
    if tr==1:
        player1='x'
        player2='0'
    else:
        player1='0'
        player2='x'
    while True:
            print("player 1's turn")
            player(player1)
            n=check_result(player1,player2)
            if n==1:
                sys.exit()
            print("player 2's turn")
            player(player2)
            n=check_result(player1,player2)
            if n==1:
                sys.exit()
def player(p):
    print("choose an empty space from 1-9")
    t=int(input())
    if game[t-1]!=' ':
        print("spaces not empty")
        player(p)
    else:
        game[t-1]=p
        print_game()

def print_game():
    
    os.system('cls')
    print(game[0]+"| "+game[1]+"| "+game[2])
    print("_|_ |_")
    print(game[3]+"| "+game[4]+"| "+game[5])
    print("_|_ |_")
    print(game[6]+"| "+game[7]+"| "+game[8])
    print(" |  | ")

def check_result(player1,player2):
    value=6
    for i in range(9):
        if game[i]==" ":
            game[i]=6
    solution1=list(set((game[0],game[4],game[8])))
    solution2=list(set((game[0],game[3],game[6])))
    solution3=list(set((game[1],game[4],game[7])))
    solution4=list(set((game[3],game[4],game[5])))
    solution5=list(set((game[2],game[5],game[8])))
    solution6=list(set((game[2],game[4],game[6])))
    solution7=list(set((game[6],game[7],game[8])))
    solution8=list(set((game[0],game[1],game[2])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
    for i in range(8):
        if len(result[i])==1 and result[i][0]!=6:
            if result[i][0]==player1:
                print("player 1 wins")
            else:
                print("player 2 wins")
            value=5 
    for i in range(9):
        if game[i]==6:
            game[i]=" "
    if(value==5):
        return 1
    else:
        return 2
print("the pattern of tic tac toe board is as follows")
print("1|2|3")
print("_|_|_")
print("4|5|6")
print("_|_|_")
print("7|8|9")
begin()