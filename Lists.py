# -*- coding: utf-8 -*-


"""
@Lesson Four Lists
@Dec 6th 2020
@Author Lawrie Scott

@TestList=[elements1, elemets2, elements]
@TestList= [0,1,2] Indexing
@sqaure brackets indicate a list
@list index out of range (Exceeding list range)
"""

myUniqueList=["Test", "Painful"]
myLeftOvers=[]

varAdd="Painful" #This word will return True

#function to test for true or false comparison to myUniqueList
def listAdd(myUniqueList):
    y=0
    x=len(myUniqueList) #Calculate length of list for looping test to each value
    while y<x:
        testVal=myUniqueList[y]==varAdd
        y+=1
    if testVal==True:
         myLeftOvers.append(varAdd)
    else:
        myUniqueList.append(varAdd)   
    
    return testVal

testVal=listAdd(myUniqueList)

#Output the value of the comaprison to the screen for TRUE Value
print("This result should be TRUE so no Appending")
print(testVal) 
print("My Unique List ")
print(myUniqueList)
print("My Left Overs List ")
print(myLeftOvers)

varAdd="Painless" #his word will return False

testVal=listAdd(myUniqueList)
#Output the value of the comaprison to the screen for FASLE Value
print()
print("This result should be FALSE Should Append")
print(testVal)
print("My Unique List ")
print(myUniqueList)
print("My Left Overs List ")
print(myLeftOvers)