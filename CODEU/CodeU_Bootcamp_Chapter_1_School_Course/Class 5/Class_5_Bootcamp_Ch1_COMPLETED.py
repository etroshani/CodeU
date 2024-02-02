#Welcome to your 5th CODEU class!


####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       -Input() Function
#       -Conditionals: If, Elif, and Else statements


##   REVIEW HOMEWORK   ##

###     HOMEWORK SOLUTION     ###

# Print your question!
print('What company has built the first rocket to ever land back on Earth undamaged?')

# Define a variable for the player’s answer
answer = input('Your answer: ')

# Conditional IF
if answer == "spacex":
     print("\nThat is the correct answer! You win!")

# Conditional ELSE
else:
     print("\nYour answer is incorrect…You lose!")




####    SECOND PART    ####

##   1) Introduction to Operators   ## 
# This will be very useful in CONDITIONALS!
5 == 6          #Meaning of '==' --> is equal to

5 < 6           #Meaning of '<' --> less than

5 > 4           #Meaning of '>' --> greater than

5 <= 6          #Meaning of '<=' --> less than or is equal to

x = 5 >= 5      #Meaning of '>-' --> greater than or is equal to

5 != 6          #Meaning of '!=' --> is NOT equal to


##   2) Continuation of Conditionals   ##

# Example 1: Greater or Smaller?
x = 10
if x < 100:
    print(x + " is smaller than 100")
elif x > 100:
    print(x + " is bigger than 100")
elif x == 100:
    print(x + " is equal to 100")
else: 
    print(x + " is not a number")


# Example 2: Are you old enough to ride the rollercoaster?
# Here, we combine input() with conditionals! 
age = input("How old are you?: ")
if int(age) >= 10:
    print("Congratulations! You are old enough to ride!")
elif int(age) < 10:
    print("Sorry! You are still too young to ride the rollercoaster :(")


###     HOMEWORK   |    Player vs Bear! ###

#   Homework Description   #
# Nintendo has asked you to create a level for their video-game. The video-game is a fighting game where, on this level,  
# the player is faced with a giant Bear and must decide what to do. They player has 3 choices: To attack, to dodge, or to scream. 
#   1) If the player attacks, the bear dies. 
#   2) If the player dodges, they dodge the bear's attack. 
#   3) If the player screams, the bear attacks and they lose the game.

#   STEPS   #
#       1) Define a variable for the player’s choice using the input() function.
#       2) Create the 1st conditional: if the player’s choice is attack, print out “You have defeated the bear!”
#       3) Create the 2nd conditional: elif the player’s choice is dodge, print out “You have dodged the bear’s attack and managed to escape!”
#       4) Create the 3rd conditional: elif the player’s choice is to scream, print out “The bear has attacked you and you lost!”
#       5) Create the last conditional: else -> the player’s choice doesn’t match the given choices, so print out ”Your choice doesn’t match any available choice…You lose!”



###     HOMEWORK SOLUTION     ###

# Define a variable for the player’s choice
print("You are faced with the giant Nintendo Bear! You must decide what to do quickly!")

playerChoice = input("You can attack, dodge, or scream. Choose now: ")

# Conditionals
if playerChoice == "attack":
     print("You chose to attack, and you have defeated the bear!")

elif playerChoice == "dodge":
     print("You have dodged the bear’s attack and managed to escape!")

elif playerChoice == "scream":
     print("The bear has attacked you and you have lost!")

else:
     print("Your choice doesn’t match any available actions…You lose!")

