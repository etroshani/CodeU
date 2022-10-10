#Welcome to your 3rd CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own.


## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


#   In the 3rd class, we are covering these topics:
#       Conditionals: If, Elif, Else
#       Time Module



####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       -Input()
#       -Float
#       -Conditionals


##   REVIEW HOMEWORK   ##
# Review the homework to correct any mistake they may have done or to answer any question they may have.


####    SECOND PART    ####

##     1) Exercise - Science Query: How well do you know your planets?      ##

print("Welcome to a Science Query on Planets! You must answer the following questions correctly.")
print("\nLet's see how well you know your solar system...")
q1 = input("\nWhat does the Earth rotate around?: ")
if q1 == "sun":
    print("\nCorrect answer!")
else:
    print("\nYour answer is INCORRECT!")

q2 = input("\nWhich planet has rings?: ")
if q2 == "saturn":
    print("\nYou are correct!")
else:
    print("\nYour answer is INCORRECT!")

q3 = input("\nWhat planet are we currently considering living on (other than earth)?: ")
if q3 == "mars":
    print("\nYou are correct!")
else:
    print("\nYou are INCORRECT!")

print("\nYou have completed the CodeU Science Query! Good job :)")


####        2) Exercise of the day: JUMANJI        ####
# You have to create your own JUMANJI Adventure. You create a character with a NAME, AGE and WEIGHT using INPUT.
# That character then has to face challenges in the jungle where they are always given 2 choices. Ultimately, one of the
# choices leads to losing the game and the game ends. The other choice leads to the next challenges.
# REQUIREMENTS:
#       -There has to be 3 challenges MINIMUM
#       -There are 2 choices per challenge
#       -Make it creative and FUN! 

#The code has already been written, but I encourage you to come up with new ideas! You can personalize it to the student's
#interests! Have fun with it :)

import time #Explain the TIME module and how it can be used

print("Welcome to Jumanji!")
time.sleep(2)
print("\nLong ago, the island of JUMANJI was a happy and prosperous place for life.")
time.sleep(3)
print("\nAnimals and plants lived in harmony, and the entire island was a heavenly location.")
time.sleep(3)
print("\nUntil one day...")
time.sleep(2)
print("\nA group of money-hungry adventurers decided to hunt down the powerful and valuable ruby...")
time.sleep(3)
print("\nAfter weeks of restless search, the found it...and took it!")
time.sleep(3)
print("\nOn their way back to their car, one of the adventurers got greedy...")
time.sleep(3)
print("\nHe attacked his coworkers and stole the ruby for himself!")
time.sleep(3)
print("\nAs he was escaping by the mountains, he tripped and dropped the ruby down the cliff, into a deep dark cave")
time.sleep(3)
print("\nAnd the ruby was never seen again...")
time.sleep(3)
print("\nThe island of JUMANJI has, since then, started to lose its life little by little, day by day.")
time.sleep(3)
print("\nThe island will soon die unless YOU can find the ruby and save JUMANJI!")
time.sleep(3)
print("\nYou must enter the island and complete the challenges ahead without dying to fetch back the lost ruby of JUMANJI")
time.sleep(2)

# First Question: Will you play?
print("\nDo you wish to enter JUMANJI in hopes of saving the island? ")
q1 = input("\nEnter yes or no: ")
if q1 == "yes":
    print("\nYou are a courageous adventurer. May all the luck be with you...and save JUMANJI!")
    time.sleep(3)

    # Second Question: Pit of Snakes!
    print("\nYou are faced with a pit of snakes. You can either fight them or jump over them. ")
    q2 = input("\nChoose jump or fight: ")
    if q2 == "jump":
        print("\nYou fell into the pit and got eaten by snakes! You lost the game...")
    
    elif q2 == "fight":
        print("\nTurns out that the snakes are terrifed of fights! As soon as you were about to engage, they fled! ")
        time.sleep(3)
        print("\nYour journey continues...")
        time.sleep(2)

        # Third Question: 
        print("\nAfter a long walk, the road you are on splits in two. You must decide wether to go left or right.")
        time.sleep(3)
        print("\nThe path on the right is dark and scary. The one on the left is sunny and bright. Choose wisely...")
        q3 = input("\nEnter left or right:")
        if q3 == "left":
            print("\nAs you enter the left path, you get stuck in quicksand and can't get back out...")
            time.sleep(2)
            print("\nYour journey on JUMANJI has come to an end...")
        elif q3 == "right":
            print("\nYou have chosen...")
            time.sleep(2)
            print("\nWisely")
            time.sleep(2)
            print("\nYour journey continues!")
            time.sleep(2)
            print("\nAs you approach a cliff, you see a shiny red rock...It's the ruby!")
            time.sleep(3)
            print("\nTo reach it, you must go down the very unstable rocky cliff, and you don't know which rockes are safe to walk on")
            time.sleep(4)

            # Fourth Question: Pick your guide
            print("\nYou must choose between a hungry lion and a monkey to guide you through. ")
            q4 = input("\nChoose monkey or lion: ")
            if q4 == "monkey":
                print("\nYou have chosen")
                time.sleep(2)
                print("\nPoorly...The monkey was devious and decided to make you step on an unstable rock to make you fall")
            elif q4 == "lion":
                print("\nYou chose the lion who is very hungry for some...")
                time.sleep(3)
                print("\nCABBAGE! That's right, the lion is a vegetarian!")
                time.sleep(3)
                print("\nCONGRATULATIONS!! You have successfully retreived the ruby and have saved JUMANJI!!")
                time.sleep(3)
                print("\nThank you for playing!")

            else:
                print("\nThat was not in the choices!")
        
        else:
            print("\That was not in the choices.")

    else:
        print("Your answer is unclear...")

elif q1 == "no":
    print("That is unfortunate...Maybe the next adventurer will have the courage to face...")
    time.sleep(3)
    print("JUMANJI!")

else:
    print("Your answer is unclear...")
        





####    HOMEWORK: Create your own ICE CREAM STORE!    ####

#   You will build an ice-cream store where clients will walk in and be welcomed!
#   1) You must give your store a name
#   2) Customers will then have the choice of Chocolate and Vanilla ice cream.
#   3) They can choose between 3 sizes: Small(s), Medium(m) and Large(l)
#   4) You must let them know their total once they have ordered!
#   Here are the prices:
#   | Vanilla |
#       Small : 2$
#       Medium : 5$
#       Large : 10$ However, it's currently OUT OF STOCK
#   | Chocolate |
#       Small : 3$
#       Medium : 10$ However, they ordered the 100th medium chocolate ice-cream today so they get it for free!
#       Large : 30$


####    HOMEWORK CORRECTION    ####
# Define your store name using INPUT() and welcome your guests to the store. Include your store name in the welcome message.
name = input("What will be your store name?: ")
print("\nHi! Welcome to " + name)

# Define the flavor ice cream the customer wants using INPUT()
icecream = input("\nWhat flavor ice-cream would you like? vanilla | chocolate: ")

# Define the size the customer wants using INPUT()
size = input("What size cone would you like? small | medium | large: ")

# Write the conditionals for ALL possible combinations
if icecream == "vanilla":
    if size == "small":
        print("\nYour total will be 2$")
    elif size == "medium":
        print("\nYour total will be 5$")
    elif size == "large":
        print("\nSorry, we don't have enough vanill ice cream left for a large...")
elif icecream == "chocolate":
    if size == "small":
        print("\nYour total will be 3$")
    elif size == "m":
        print("\nCongratulations! You are our 100th medium chocolate ice-cream ordered today! It's free!")
    elif size == "l":
        print("\nYour total will be 30$")
else:
    print("Sorry, we don't have that at " + name)
