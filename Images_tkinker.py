from tkinter import * 
from PIL import ImageTk, Image
import getpass
import random 
from collections import Counter 

root=Tk()
root.iconbitmap("C:\\Users\\Lawrie Scott\\Pictures\\LockIcon.ico")



someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

Player1_Status = True
Player1 = True

someWords = someWords.split(' ') 
if Player1 == True:    
    # randomly choose a secret word from our "someWords" LIST. 
    Player1_word = random.choice(someWords)		 

    if __name__ == '__main__': 
        print('Guess the word! HINT: word is a name of a fruit') 
        
        for i in Player1_word: 
            # For printing the empty spaces for letters of the word 
            print('_', end = ' ')		 
        print() 

        playing = True
        # list for storing the letters guessed by the player 
        letterGuessed = ''				 
        chances = len(Player1_word) + 2
        correct = 0
        flag = 0
        try: 
            while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed 
                print() 
                chances -= 1

                try: 
                    guess = str(input('Enter a letter to guess: ')) 
                except: 
                    print('Enter only a letter!') 
                    continue

                # Validation of the guess 
                if not guess.isalpha(): 
                    print('Enter only a LETTER') 
                    continue
                elif len(guess) > 1: 
                    print('Enter only a SINGLE letter') 
                    continue
                elif guess in letterGuessed: 
                    print('You have already guessed that letter') 
                    continue

                # If letter is guessed correctly 
                if guess in Player1_word: 
                    k = Player1_word.count(guess) #k stores the number of times the guessed letter occurs in the word 
                    for _ in range(k):	 
                        letterGuessed += guess # The guess letter is added as many times as it occurs 

                # Print the word 
                for char in Player1_word: 
                    if char in letterGuessed and (Counter(letterGuessed) != Counter(Player1_word)): 
                        print(char, end = ' ') 
                        correct += 1
                    # If user has guessed all the letters 
                    elif (Counter(letterGuessed) == Counter(Player1_word)): # Once the correct word is guessed fully, 
                                                                    # the game ends, even if chances remain 
                        print("The word is: ", end=' ') 
                        print(Player1_word) 
                        flag = 1
                        Player1_Status=False
                        print('Congratulations, You won!') 
                        break # To break out of the for loop 
                        break # To break out of the while loop 
                    else: 
                        
                        print('_', end = ' ') 

                # If user has used all of his chances 
                if chances <= 0 and (Counter(letterGuessed) != Counter(Player1_word)): 
                    # *******************************************************************************************
                    # Change the window Icon
                    my_Image = ImageTk.PhotoImage(Image.open("C:\\Users\\Lawrie Scott\\Pictures\\HangmanLose.jpg"))
                    my_Image_Label= Label(image=my_Image)
                    my_Image_Label.pack()
                    TheWord=('The word was {}'.format(Player1_word))
                    TheWord=Label(text=TheWord, fg="black", bg="red", font=(None, 12))
                    TheWord.pack() 
                    root.mainloop()

        except KeyboardInterrupt: 
            print() 
            print('Bye! Try again.') 
            exit() 
