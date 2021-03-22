# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:17:44 2020

@author: lawrie Scott
@Title: Song Choices Favourite Song Breakdown

The purpose of thiss short program to demonstrate variables and some basic uses of them
"""
import os

FileCreation = "Created on Thu Dec  3 16:17:44 2020"
print("Welcome " + os.getlogin() + " To Larie's Song Project")
print()


#Setup song variables long method

SongTitle="Carl Orff: Carmina Burana" #String Variable
Artist="University of Califonia" #String Variable
Orginal="No" #String Variable
Genre="classical music repertoire" #String Variable
YearRealeased=2008 #Integer
Year=str(YearRealeased) #Integer to String conversion for concatination
Awards = "Yes" #String Variable
YouTubeUrl ="https://www.youtube.com/watch?v=QEllLECo4OM" #String Variable
NumberOfViews=20779463 #Integer
Views=str(NumberOfViews) #Integer to String conversion for concatination
Overview="Carl Orff's Carmina Burana is one of the most popular pieces of the classical music repertoire. Here the UC Davis Symphony Orchestra, the University Chorus and Alumni Chorus, and the Pacific Boychoir perform at the Mondavi Center at UC Davis."

print ("Title - " + SongTitle)
print("Artist - " + Artist)
print("Original Score - " + Orginal)
print("Genre - " + Genre)
print("Any Awards - " + Awards)
print("YouTube URL - " + YouTubeUrl)

#Setup song variables short method Showing only short string variables
SongTitle, Artist, Orginal, Genre, Awards = "Carl Orff: Carmina Burana, Pacific Boychoir", "University of Califonia", "No", "classical music repertoire", "No"

#print again short string variables to test shorthand Changed variables and description strings Here
print()
print ("Title - " + SongTitle)
print("Orchestra & Choir - " + Artist)
print("Score - " + Orginal)
print("Genre - " + Genre)
print("Awards - " + Awards)


#Working with Integers
print()
print("Printing Integer Values")
print("Year Released- ") 
print(YearRealeased)
print("Number of Views- ")
print(NumberOfViews)

#Concatenate converted Integers and Strings
print()
print("Combine fields into a sentence using converted Integer Variables")
print("Number of View Since " + Views + "," + " Release Date " + Year) 

#The Song Overview
print()
print(Overview)