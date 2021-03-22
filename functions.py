# -*- coding: utf-8 -*-


"""
@Lesson Two Functions
@Class work to reuse the Below Music Example from Lesson One
@Dec 4th 2020
@Author Lawrie Scott

"""
#Setup Global variables
SongTitle="Carl Orff: Carmina Burana" #String Variable
Artist="University of Califonia" #String Variable
OrgVer=1935 #Boolean Variable will be passed as integer
Genre="classical music repertoire" #String Variable
YearRealeased=2008 #Integer

#Define my function to capture information using global variables
def music(Song, Singer, MusicType, YearMade):
    Song=SongTitle
    Singer=Artist
    MusicType=Genre
    YearMade = str(YearRealeased) #convert Integer to string
    output = "The song " + Song + " released " + YearMade + " by " + Singer + " in the Genre " + MusicType
    return output

#Calculate the true or false based on OrgVer Matching Release Date of music and using comparison create a boolean output
Org=False
if OrgVer == YearRealeased : Org=True

#Structure the output for printing
song=music(SongTitle, Artist, Genre, YearRealeased)
#Formatting the boolean for use in print output
Original = " it is {}".format(Org) + " that this is an orginal score."
orgVersion = str(OrgVer)

print(song + Original + " The orginal was released " + orgVersion)

