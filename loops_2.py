# -*- coding: utf-8 -*-


"""
@Lesson Five Loops
@Dec 7th 2020
@Author Lawrie Scott
@2nd Assignment for this topic (shapes
                                )

"""
# -*- coding: utf-8 -*-


"""
@Lesson Five Loops
@Dec 7th 2020
@Author Lawrie Scott
@2nd Assignment for this topic (shapes
                                )

"""
import textwrap

#Produce a Chess Board 8x8 Squares
#Place Chess Pieces for White and Black

dashCount = 49
rangeReq=16 #this is the range needed for my 8x8 squares

print("-"*dashCount)

for row in range(16): 
    if row%2 == 0: #0, 
        
        for col in range(1, 9):#1, 2
            
            if row == 0:
                if col == 1:
                    print("|", end="")
                    print("  @  |", end="")
                elif col != 1:
                    print("  @  |", end="")

            if row == 2:
                if col == 1:
                    print("|", end="")
                    print("  @  |", end="")
                elif col != 1:
                    print("  @  |", end="")

            if row == 12:
                if col == 1:
                    print("|", end="")
                    print("  X  |", end="")
                elif col != 1:
                    print("  X  |", end="")

            if row == 14:
                if col == 1:
                    print("|", end="")
                    print("  X  |", end="")
                elif col != 1:
                    print("  X  |", end="")

            if row == 4 or row == 6 or row == 8 or row == 10:
                if col == 1:
                    print("|", end="")
                    print("     |", end="")
                elif col != 1:
                    print("     |", end="")
    else:
        print()
        print("-"*dashCount)
        
    if row >= 16-1:
        print()
        print("True")

    


#Assumption on Screen Size is 200 and Height is 45
#Check for screen looping and force text to wrap at 80 Characters

screenWidth = 200
screenWrap=80

#Create a string longer than 200 characters for testing

testStr="Sports car aficionados might scoff at Nissan labeling the 2020 Nissan Maxima as a four-door sports car — two more doors than a sports car should have, they would say — but the claim isn't entirely without merit. The Maxima handles with more verve than many of its midsize sedan rivals, and its standard V6 engine generates a healthy 300 horsepower. Plus, it comes from the same company that makes the world-beating GT-R Nismo and legendary 370Z sports cars, so there's a bona-fide legacy in the claim. Beyond the Maxima's sharp design and bold grille, you'll find a comfortable cabin with intuitive controls, stylish trim and, in the case of the SR trim level, a combination of leather upholstery, simulated-suede seat inserts and contrasting orange stitching. Few things change for 2020, but the Maxima adds several driver aids and improved ride and handling to the standard equipment list and a sunroof to the SR model. It's the Maxima's dual sport-and-luxury concept that explains its primary appeal but also reveals its flaws. There are rivals that are roomier, carry more cargo, and offer similar performance for much less money. The Maxima also trails even its own family sedan counterpart, the Nissan Altima, when it comes to up-to-date infotainment tech and driver aids. But if you're seeking a performance-oriented sedan with impressive abilities on a twisting road, the Maxima is worth a look."

if len(testStr) > screenWidth:
    wrapper = textwrap.TextWrapper(width=screenWrap) # Wrap this text. 
    word_list = wrapper.wrap(text=testStr) #Create a  list to print  
  
# Print each line. 
print() #Just used to create a gap
for element in word_list: #print out the wordlist varaible
    print(element) 


