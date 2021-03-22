# -*- coding: utf-8 -*-


"""
@Lesson Three IF Statements
@Class work to reuse the Below Music Example from Lesson One
@Dec 5th 2020
@Author Lawrie Scott

"""
#Setup Global variables
Artist="University of Califonia" #String Variable
OrgVer=1935 #Boolean Variable will be passed as integer
YearRealeased="2008" #Integer as String
OrginalArtist="Carl Orff"
stringDate="Year First Release 1935"


#Function to prove False or True if Both eequal   
def music(Singer, OrgVersion, Release, OrgSinger):
    
    #Comapring orginal Version and Orginal Date 'AND' Artists
    if OrgVer == int(YearRealeased) and Artist == OrginalArtist:
        notEq="True"
        
    else:
        notEq="False"
        
    return notEq

notEq=music(Artist, OrgVer, YearRealeased, OrginalArtist)
print(notEq)


#Function to prove False or True one or Both eequal to ensure Integer conversion working
YearRealeased="1935" #change variabke to get an equal value between integer and string
def music(Singer, OrgVersion, Release, OrgSinger):
    
    #Comapring orginal Version and Orginal Date 'OR'' artists
    if OrgVer == int(YearRealeased) or Artist == OrginalArtist:
        oneEq="True"
        
    else:
        oneEq="False"
        
    return oneEq

oneEq=music(Artist, OrgVer, YearRealeased, OrginalArtist)
print(oneEq)

#reset value of YearReleased variable
YearRealeased="2008"