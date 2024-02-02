####    FIRST PART    ####

# Recap of Class 4 theory: 
#       Loops: While
#       Random Module    

###     HOMEWORK SOLUTION     ###

import random

boss_lives = 5

while boss_lives != 0:
    boss_nb = random.randrange(1,10)
    player_nb = int(input("What is your guess: "))

    if boss_nb == player_nb:
        print("You and the final boss both guessed: " + boss_nb)
        print("\nYour attack was successful!")
        boss_lives -= 1

print("\nYou have defeated the boss!")



####    SECOND PART    ####


##     Introduction to Loops: FOR     ##

# We want to print all elements of a list. This method works, however it is not ideal if our list contains many elements.
fruits = ["apple", "banana", "strawberry", "mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Instead, we use FOR loop to retrieve the elements in a list
fruits = ["apple", "banana", "strawberry", "mango"]
for i in fruits:
    print(i)

# Find the SUM of all the elements in a list
numbers = [1, 4, 8, 12]
total = 0
for i in numbers:
    total += i
print(total)

# Finding each element of a String
name = "Sebastian"
for i in name:
    print(i)

# Introduction to RANGE()
for i in range(5):
    print(i)

# range(START, STOP, STEP). The first value is the start of the range, the second is the end of the range, and the third is the increment of the step.
for i in range(5,15,3):
    print(i)


####    HOMEWORK: Will the elevator break?    ####

#   A famous hotel in New York City has a faulty and very weak elevator. They've held back on fixing it
#   because they are lazy and don't want to spend money. 
#   By precaution, the can only allow 8 people on the elevator at a time.
#   A group of tourists arrive at the hotel. They all book a room for the night. Since they're all together,
#   they decide to go up at the same time. We have the weight of each person in pounds:
#   208, 200, 350, 500, 127, 145, 134, 900
#   The elevator can only hold a MAXIMUM of 2500 pounds. You must determine if the elevator will break
#   if they all use it at the same time!

#   1) You must create a list with all weights
#   2) You will then define a variable for the total weight.
#   3) You must use a FOR Loop to navigate the list you made
#   4) Add each individual weight to the variable for total weight
#   5) Print() the total weight once the loop is complete
#   6) Print() the number of people on the elevator using a list method



####    YOUR CODE    ####

# 1) Create a list with all the weights


# 2) Define a variable for the total weight. This is where we will add all the weights.
#    It will initially be equal to 0



# 3) Create a FOR loop that will navigate the list of weights. Add the weights to the variable of the total weight.



# 4) Print the total weights once the loop is complete


# 5) Print the number of people on the elevator



