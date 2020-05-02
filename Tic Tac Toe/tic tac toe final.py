import os
import sys
import random 
game=[" "," "," "," "," "," "," "," "," "]
def isspacefree(board,index):
    return game[index]==" "

def again(player1):
        t=int(input())
        if isspacefree(game,(t-1)):
            game[t-1]=player1
            print_game()
        else:
            again()

def print_game():
    
    os.system('cls')
    print(game[0]+"| "+game[1]+"| "+game[2])
    print("_|_ |_")
    print(game[3]+"| "+game[4]+"| "+game[5])
    print("_|_ |_")
    print(game[6]+"| "+game[7]+"| "+game[8])
    print(" |  | ")

def checkresult(bo,p):
    solution1=list(set((bo[0],bo[4],bo[8])))
    solution2=list(set((bo[0],bo[3],bo[6])))
    solution3=list(set((bo[1],bo[4],bo[7])))
    solution4=list(set((bo[3],bo[4],bo[5])))
    solution5=list(set((bo[2],bo[5],bo[8])))
    solution6=list(set((bo[2],bo[4],bo[6])))
    solution7=list(set((bo[6],bo[7],bo[8])))
    solution8=list(set((bo[0],bo[1],bo[2])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
#    print(result)
    for i in range(8):
        if len(result[i])==1 and result[i][0]!=" ":
            if result[i][0]==p:
                return True
            else:
                return False
def makemove(i,player2):
    game[i]=player2
    
def randomchoice(board,a):
      possibleMoves = []
      for i in a:
          if isspacefree(board, i):
            possibleMoves.append(i)
      if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
      else:
        return None
    
def computer(player1,player2):
    for i in range(0,9):  
        copy=[]
        for j in range(0,9):
            copy.append(game[j])
        if isspacefree(copy,i):
            copy[i]=player2
            if checkresult(copy,player2):
                print("position",i)
                return i    
    for i in range(0,9):  
        copy=[]
        for j in range(0,9):
            copy.append(game[j])    
        if isspacefree(copy,i):
            copy[i]=player1
            if checkresult(copy,player1):
                return i  
    move=randomchoice(game,[0,2,6,8])
    if move!=None:
         return move
    elif isspacefree(game,5):
         return 5
    else:
         return randomchoice(game,[2,4,6,8])
def begin():
    print("press\n 1) player1='x' and player2='0'\n 2) player1='0' and player2='x'")
    tr=int(input())
    if tr==1:
        player1='x'
        player2='0'
    else:
        player1='0'
        player2='x'
    print("player1 =",player1+"\nplayer2 =",player2) 
    while True:
        print("---------------\n")
        print("player1's turn")
        print("choose an empty space from 1-9")
        again(player1)
        if checkresult(game,player1):
            print("player 1 wins")
            sys.exit()
        print("computer's turn")
        pos=computer(player1,player2)
        makemove(pos,player2)
        print_game()
        if checkresult(game,player2):
            print("computer wins")
            sys.exit()
        
print("welcome to the game!!!")
print("pattern")
print("1|2|3")
print("_|_|_")
print("4|5|6")
print("_|_|_")
print("7|8|9")
begin() 