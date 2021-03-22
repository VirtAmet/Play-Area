import random
from colorama import init, Fore, Back, Style
import time
import sys

output=[]
player=[]
player_lives=7

wordList="bangkok beijing colombo nairobi baghdad algiers caracas jakarta kampala"
print("HINT: Country capitals: \n")

def TheGame(thePlayer):
    Words = wordList.split(" ")
    Mystery_Word = random.choice(Words)

# Print out the blank letter spaces
    j=0
    global playerWord
    playerWord=""
    newLetter=""
    output=[]
    for i in Mystery_Word: 
        # The empty spaces for letters of the word 
        output.append("_")
        newLetter=output[j]		 
        playerWord=playerWord + newLetter
        j += 1
    print("\n Word " + playerWord + "Consists of " + str(len(playerWord)) + " Characters\n")
    startTime=0
    startTime=time.localtime()[5]
    chances=len(Mystery_Word)+2
    while playerWord != Mystery_Word:
        guess=""
        guess=input(str("Input you guess in lowercase: "))
        guess=str.lower(guess)
        x=0
        if guess in Mystery_Word:
            for char in Mystery_Word:
                if char in guess and output[x] == "_":
                    output[x]=char
                x+=1    
            k=0
            playerWord=""
            while k != len(output):
                playerWord = playerWord + output[k]
                k+=1
        print(playerWord)

#This function is used to print the progress through visuals
        if guess not in Mystery_Word:
            global player_lives
            player_lives=player_lives-1
            k=0
            playerWord=""
            while k != len(output):
                playerWord = playerWord + output[k]
                k+=1
            hanging=visuals(player_lives)
            print(hanging)
            if player_lives==0:
                sys.exit()

        if playerWord == Mystery_Word:
            finishTime=time.localtime()[5]
            playerTime=0
            playerTime=finishTime-startTime
            if playerTime<0:
                playerTime=60-playerTime
            print(Fore.RESET)
            player[thePlayer]=playerTime
            break
        # else:
            # chances -= 1

    if chances==0 and playerWord != Mystery_Word:
        finishTime=time.localtime()[5]
        playerTime=0
        playerTime=finishTime-startTime
        if playerTime<0:
            playerTime=60-playerTime
        print(Fore.RESET)
    # playerCount
    return

def visuals(player_lives):
#This function is used to print the progress through visuals
	if player_lives == 6:
		return"""
		_______
		|     |
		|     
		|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 5:
		return"""
		_______
		|     |
		|     O
		|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 4:
		return"""
		_______
		|     |
		|     O
		|   --|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 3:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 2:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    |
		|
		|________
		|        |
		"""
	elif player_lives == 1:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    | |
		|
		|________
		|        |
		"""
	elif player_lives == 0:
		return"""
		_______
		|     |
		|     l0
		|    |||
		|     |
		|    | |
		|
		|________
		| D E A D|
		"""	


# Calling the word and program to start

playerCount=int(input("Enter Number of Players, the player with the best time wins: "))
p=playerCount
while p != 0:
    player.append(p)
    p -= 1
z=0
while z < playerCount:
    thePlayer=z
    TheGame(thePlayer)
    z += 1
while z > p:
    z -= 1
    print(Fore.GREEN, "Player ", z+1, "'s time is ", player[z], " seconds. \n")
print(Fore.RESET)