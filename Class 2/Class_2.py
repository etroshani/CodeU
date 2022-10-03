#Welcome to your 2nd CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own.


## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


#   In the 2nd class, we are covering these topics:
#       -Input()
#       -Float
#       -Conditionals



####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       -print()
#       -Defining variables
#       -Mathematical equations and operations: Using Python as a calculator
#       -Strings, Integers, Floats and Booleans
#       -Input


##   REVIEW HOMEWORK   ##
# Review the homework to correct any mistake they may have done or to answer any question they may have.



####    SECOND PART    ####

##   1) Continuation of INPUT    ##

# Example: What year are you born in?
age = input("How old are you?: ") 
dateofbirth = 2022 - int(age)
print(name + " is born in " + str(dateofbirth))

##   Small Exercise: What is the exact weight of an ant colony?   ##
#   **Float is important here**
print("\nYou face a colony of ants. The average ant weighs about 0.225 pounds. There is about 300 ants in front of you.")
print("You have to calculate the EXACT total weight of the colony\n")
weight = input("How much does an average ant weigh?: ")
nbAnts = input("How many ants are there?: ")
product = float(weight)*float(nbAnts)
print("The colony of ants weigh exactly" + product + " pounds")

#   Is it possible to combine a float with an Int?
combine = float(weight)*int(nbAnts)
print(combine)


##   Big Exercise: Creating a list of VIP guests using name, age and height  ##
#   You are the host of the annual CodeU birthday bash! You are given the responsibility of creating a small VIP guest list
#   Unfortunately, there can only be 3 VIP guests this year. You must take down each guests NAME, AGE, and HEIGHT(cm)
#   Create a list using INPUT and PRINT

#   VIP #1   #
person1 = input("Enter name of VIP #1: ")
person1_age = input("Enter age of "+ person1 + ": ")
person1_height = input("Enter height in cm of "+ person1 + ": ")

#   VIP #2   #
person2 = input("Enter name of VIP #2: ")
person2_age = input("Enter age of "+ person2 + ": ")
person2_height = input("Enter height in cm of "+ person2 + ": ")

#   VIP #3   #
person3 = input("Enter name: ")
person3_age = input("Enter age of "+ person3 + ": ")
person3_height = input("Enter height in cm of "+ person3 + ": ")

#   Print all VIP members with their attributes   #
print("\nHere is the VIP Guest List")
print("\nVIP #1")
print(person1 + "\n" + "Age: "+ person1_age + "\nHeight: " + person1_height + " cm \n")
print("\nVIP #2")
print(person2 + "\n" + "Age: "+ person2_age + "\nHeight: " + person2_height + " cm \n")
print("\nVIP #3")
print(person3 + "\n" + "Age: "+ person3_age + "\nHeight: " + person3_height + " cm")
print("\nVIP list is complete! Have a wonderful CodeU Birthday BASH!!")




##     2) Introduction to CONDITIONALS     ##

# Explain the functionality of CONDITIONALS. How they work and when to use them.

# Example 1
animal = "cow"
if animal == "cow":
    print("MOO!!")
elif animal == "cat":
    print("Miaow!!")
elif animal == "dog":
    print("WOOF!")
else:
    print("That is not an animal!")


# Example 2
x = 10
if x < 100:
    print(x + " is smaller than 100")
elif x > 100:
    print(x + " is bigger than 100")
elif x == 100:
    print(x + " is equal to 100")
else: 
    print(x + " is not a number")


# Small exercise using INPUT: Are you old enough to ride the rollercoaster? 
age = input("How old are you?: ")
if int(age) >= 10:
    print("Congratulations! You are old enough to ride!")
elif int(age) < 10:
    print("Sorry! You are still too young to ride the rollercoaster :(")
else:
    print("That is not a number")



###        HOMEWORK        ###
#   For your birthday party, you have a VIP section. Only 2 people are allowed to TRY to enter. To enter, 
#   they must guess the correct number between 1 and 5 that YOU choose using INPUT().You must take down their 
#   First Names, Last Names, and their guess. 

#   1) Welcome your guests!
#   2) Define a variable with a number between 1 and 5. Use Input()
#   3) You have a VIP section and only 2 people are allowed to TRY to enter.
#   4) You have to take down their FIRST NAMES and their GUESS. 
#   5) If they guess incorrectly, they CAN'T be part of the VIP list. You must let them know they can't be a VIP member.
#   6) If they guess correctly, you must greet them using their name and welcome them to the VIP section.
#   7) Print() a message saying the VIP entrance is closed once all tries are done.


###     HOMEWORK SOLUTION     ###

# Name your birthday party
myNumber = input("What is your number between 1 and 5?: ")
print("Welcome to my birthday party!")

# First Guest
print("Guest 1: ")
guest1_firstName = input("What is your first name: ")
guest1_guess = input("What is your guess?: ")
if int(guest1_guess) != int(myNumber):
    print("Sorry, your guess was wrong! You cannot enter the VIP section :(")
elif int(guest1_guess) == int(myNumber):
    print("Welcome to the VIP section " + guest1_firstName)
else:
    print("Your guess is not a number!")

# Second Guest
print("Guest 2: ")
guest2_firstName = input("What is your first name: ")
guest2_guess = input("What is your guess?: ")
if int(guest2_guess) != int(myNumber):
    print("Sorry, your guess was wrong! You cannot enter the VIP section :(")
elif int(guest2_guess) == int(myNumber):
    print("Welcome to the VIP section " + guest2_firstName)
else:
    print("Your guess is not a number!")

# Vip is closed message
print("Thank you for trying! The VIP entrance is now closed...")














