# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 09:01:59 2021
Connect 4 Game

@author: Lawrie Scott
"""
import colorama, time, sys
gridheight=5
gridwidth=6


#prepare players colors
from colorama import Fore, Back, Style 
player1=Fore.GREEN + u'\u2B24'
player2=Fore.RED + u'\u2B24'
player=1


#Create a grid
#Test grid for full game only column 0 has 1 open slot
#grid=[[0,2,1,2,1,2,1],[1,2,1,2,1,2,1],[2,1,2,1,2,1,2],[1,2,1,2,1,2,1], \
#      [1,2,1,2,1,2,1],[2,1,2,1,2,1,2]]

#Empty grid to use
grid=[['\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤'], \
      ['\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤'], \
      ['\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤'], \
      ['\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤'], \
      ['\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤'], \
      ['\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤','\x1b[94m⬤'],]

#Grid for calculating the win
gridWin=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], \
         [0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
(grid)    
    
#print function for the grid
def gridOutput(grid):
    colNum=[0,1,2,3,4,5,6]
    print(Fore.RESET)
    tempGrid=grid
    for i in range(len(tempGrid)):
        for j in range(len(tempGrid[i])):
            print(Fore.RESET, tempGrid[i][j], end=' ')
        print()
    for x in range(len(colNum)):
        print(Fore.RESET, colNum[x], end=' ')
    print("\n")    
    return


#Function to check for a winner
output=False
def check_winner(gridWin, player):
    #check horizontal spaces
    for y in range(gridheight):
        for x in range(gridwidth - 3):
            if gridWin[x][y] == player and gridWin[x+1][y] == player and gridWin[x+2][y] == player and gridWin[x+3][y] == player:
                return True

    #check along the vertical
    for x in range(gridwidth):
        for y in range(gridheight - 3):
            if gridWin[x][y] == player and gridWin[x][y+1] == player and gridWin[x][y+2] == player and gridWin[x][y+3] == player:
                return True

    #check / diagonal spaces
    for x in range(gridwidth - 3):
        for y in range(3, gridheight):
            if gridWin[x][y] == player and gridWin[x+1][y-1] == player and gridWin[x+2][y-2] == player and gridWin[x+3][y-3] == player:
                return True

    #check \ diagonal spaces
    for x in range(gridwidth - 3):
        for y in range(gridheight - 3):
            if gridWin[x][y] == player and gridWin[x+1][y+1] == player and gridWin[x+2][y+2] == player and gridWin[x+3][y+3] == player:
                return True

    return False

while output == False:
    gridOutput(grid)
#    print(colNum, "\n")    
    print("Player ", player, "Your Move")
    value=False
    while value == False:
        backCount=int(input("Select a column: "))
        if backCount>=7:
            print("Nota a valid Column Please Try Again: ")
            value=False
        else:
            value=True
    gridSlot=5
    while gridSlot<6 and gridSlot>=-2:
        if gridSlot==-2:
            print("No winner or slots")
            sys.exit("Thansk for playing")
        if gridWin[gridSlot][backCount] == 0 and player==1:
            time.sleep(1)
            grid[gridSlot][backCount]=player1
            gridWin[gridSlot][backCount]=1
            break
        elif gridWin[gridSlot][backCount] == 0 and player==2:
            time.sleep(1)
            grid[gridSlot][backCount]=player2
            gridWin[gridSlot][backCount]=2
            break
        else:
            print(Fore.RESET)
            gridSlot-=1
            
    output = check_winner(gridWin, player)
    
    if output == True:
           winStatus="you are the winner \n"
           break
    else:
        winStatus="No winner yet \n"
        if player==1:
            player=2
        else:
            player=1 

print("Player" , player, winStatus) #convert out put to string for winner or no winner
print("The winning grid \n")
gridOutput(grid)