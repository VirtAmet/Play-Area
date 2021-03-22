# -*- coding: utf-8 -*-


"""
@Lesson Five Loops
@Dec 7th 2020
@Author Lawrie Scott
@Sets and Dictionaries

"""

#Setup song variables long method
#Orhinal variables from 1st assignment
SongTitle="Carl Orff: Carmina Burana" #String Variable
Artist="University of Califonia" #String Variable
Genre="classical music repertoire" #String Variable
YearPerformed=2008 #Integer
Year=1935


#Assignment 1 section to print out the Values and counts
print("Display of value and keys in a Dictionary", "\n")
Songs={1:"Carmina", 2:"UCLA", 3:"Classical", 4:2008, 5:1935, 2:"UCLA"}
print()
print(Songs)
print()
for value, key in Songs.items():
    print("key: ", value, end="")
    print(" Value: ", key, " ")
    print()

#Extra Credit function and compare
print("Extra credit assignment", "\n")

countryList={"FR":1, "USA":2, "UK":3, "ZA":4, "NZ":5}

countryName = input("Pleae input your Country. Please use country Abbr in UPPERCASE:\n ")
print()

def guessContry(countryName): #Defining a function to look for the inputted value
    compResult = True
    while(True):
        for key, value in countryList.items():
            if key != countryName:
                compResult = False
            else:
                compResult = True
                break
        return compResult
 
result= guessContry(countryName)  #Calling the function and passing the input
print("It is " + str(result) + " that this country exists in the Dictionary") #Printing the output to show the value status True/False
print()