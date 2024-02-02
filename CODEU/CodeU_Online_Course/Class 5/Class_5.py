#Welcome to your 5th CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own.


## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


#   In the 5th class, we are covering these topics:
#       Loops: WHILE
#       Loops: FOR




####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       Lists
#       Loops: WHILE


##   REVIEW HOMEWORK   ##
# Review the homework to correct any mistake they may have done or to answer any question they may have.



####    SECOND PART    ####


##     1) First Exercise Of The Day - Guess The Number!      ##
#   ***Explain the RANDOM Module and how we can use it.***   #
import random

x = random.randrange(1,10) #Explain what randrange() means!

number = int(input("Choose a number between 1 and 10: "))

while number != x:
    print("\nSorry, you guessed incorrectly! Try again.")
    number = int(input("Guess a number between 1 and 10: "))

print("Congratulations! You guessed correctly!")


##    2) Metaverse Guessing Contest!    ##
import random
import time


print("Welcome to Radio Metaverse Guessing Game! Today, we have a contest for you!") 
time.sleep(2)
print("\nYou must guess a number between 1 and 10. You have 3 tries to guess it correctly.") 
time.sleep(2)
print("\nIf you do...You win entrance to the METAVERSE!")
time.sleep(2) 
print("\nCall us at the Metaverse Radio Station to enter the contest.")
time.sleep(2)


tries = 3
number = random.randrange(1,10)     # Explain randrange() and what it does!
    
call = input("\nWrite 'call' to call the Radio Station: ")
    
if call == "call":
    print("Thank you for calling Radio Metaverse!")
        
    while tries > 0:
        guess = int(input("Please enter your guess: "))
        
        if guess == number:
            print("\nCongratulations!! You now have access to the METAVERSE :)")
        
        else:
            print("Sorry, you guessed incorrectly!")
            tries -= 1

else:
    print("Not a valid answer!")




##     3) Introduction to Loops: FOR     ##

# Explain the functionality of FOR Loops. How they work and when to use them.


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

# Finding each element of a String (word, sequence of letters, etc.)
name = "Sebastian"
for i in name:
    print(i)

# Introduction to RANGE()
for i in range(5):
    print(i)

# range(START, STOP, STEP). The first value is the start of the range, the second is the end of the range, and the third is the increment of the step.
for i in range(5,15,3):
    print(i)


##      Final Exercise of the day: Hidden passage in the hills!     ##

print("During a hike, you come across a hidden entrance in the mountains...")
time.sleep(2)
print("\nYou try to enter, but the entrance seems locked...")
time.sleep(2)
print("\nNext to the passage, you see a sentence engraved in the wall")
time.sleep(2)
print("\nAnd it says the following...")
time.sleep(2)
print("\nTo enter, you must find the sum of all numbers between 1 and 99")

sum = 0
for i in range(1,100):
    sum = sum + i
print(sum)

answer = input("Please enter your answer: ")
if int(answer) == 4950:
    time.sleep(2)
    print("\nYou may enter the hidden passage in the hills!")
else:
    time.sleep(2)
    print("\nThat answer is incorrect!")


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



####    HOMEWORK CORRECTION    ####

# Build the list of tourists
weight = [208, 200, 350, 500, 127, 145, 134, 900]

# Create the variable where you will be adding the weight of every person
weight_total = 0

# Create the FOR Loop
for i in weight:
    weight += i

# Print the results
participants = len(weight)
print(str(participants) + " participants weigh a total of " + str(weight_total))

