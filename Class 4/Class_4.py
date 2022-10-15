#Welcome to your 4th CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own.


## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


#   In the 4th class, we are covering these topics:
#       Lists
#       Loops: WHILE



####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       Conditionals: If, Elif, Else
#       Time Module


##   REVIEW HOMEWORK   ##
# Review the homework to correct any mistake they may have done or to answer any question they may have.



####    SECOND PART    ####

##     1) Introduction to Lists - Explain how to manipulate list and how it is useful     ##

# Printing out a list.
fruits = ["apple", "orange", "grape", "banana", "blueberry"]
print(fruits)

# Lists can contain different types of elements.
fruits = ["apple", 10, 5.4]
print(fruits)

# You can retrieve a specific element of a List using the INDEX number.
fruits = ["apple", "orange", "grape", "banana", "blueberry"]
print(fruits[0])

# A section of the list can be grabbed
print(fruits[0:2])

# Modifying an element in a list
print(fruits[1])
fruits[1] = "mandarine"
print(fruits[1])
print(fruits)

# Adding an element to the end of the list
fruits.append("watermelon")
print(fruits)

# A list can be empty. To add elements, we use append.
fruits = []
fruits.append("apple")
print(fruits)

# Adding an element at a specific position in the list
fruits = ["apple", "orange", "grape", "banana", "blueberry"]
fruits.insert(2, "watermelon")
print(fruits)

# Erasing an element in the list
fruits.remove("apple")
print(fruits)

# Detecting wether an element is in the list or not using Boolean
print("orange" in fruits)

# Finding the length of the list
print(len(fruits))



##     2) Introduction to Loops: WHILE     ##

# Explain the functionality of LOOPS. How they work and when to use them.

# Example 1 
i = 0
while i<5:
    print(i)
    i = i + 1

# Example 2
i = 10
while i>1:
    print("Hello World")
    i = i - 1

# Example 3 - Can we go to the movies?
answer = input("Can we got to the movies? ")
while answer == "no":
    answer = input("Can we got to the movies? ")

print("Yay, thank you!")


##     2) Tiny Exercise - Let's build a Countdown for the CodeU Track Race!      ##
#   ***Explain the Time Module and how we can use it.***   #

import time

print("Welcome to the annual CodeU Track Race!\n")
print("The race will now start in...")

timer = 3
while timer > 0:
    print(timer)
    timer -= 1
    time.sleep(1)

print("Go Go Go!")


####    HOMEWORK: Create your Wish List Maker!    ####

#   You will build a Wish List Maker for anyone that would like to make a list of presents they would love to receive in the future!
#   1) You must create an empty list where each gift will be added
#   2) You will then define a variable using INPUT(). This is where the user is asked what present they would like to add to the list.
#   3) The list can contain only 5 items.
#   4) Create a WHILE Loop that ends once the list LENGTH is equal to 5. 
#   5) Print() the completed list to the user



####    HOMEWORK CORRECTION    ####

# 1st Part : Create an empty list
wishlist = []

# 2nd Part : Create the WHILE Loop that ends once the list LENGTH is 5

# Explanation: The user will be asked to add a present to the list 5 separate times. This means that the same question is
#              repeated 5 times. Each answer is added to the list.
while len(wishlist) != 5:
    gift = input("What gift would you like to add to your Wish List?: ")
    wishlist.append(gift)

# 3rd Part : Print() the list
print("Here is your Wish List!")    #Do not remove this line
print(wishlist)



    
