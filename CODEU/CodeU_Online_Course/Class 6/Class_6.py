#Welcome to your 6th CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own.


## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


#   In the 6th class, we are covering these topics:
#       Loops: FOR
#       Loop controls: CONTINUE and BREAK statements




####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       Loops: WHILE
#       Loops: FOR


##   REVIEW HOMEWORK   ##
# Review the homework to correct any mistake they may have done or to answer any question they may have.



####    SECOND PART    ####
import time

##     1) First Exercise Of The Day - CodeU Amusement Park      ##
print("You've been hired by the CodeU Amusement Park to help them out with some information")
time.sleep(2)
print("They've given you a list of people's heights and asked you to determine how many people there are, and how many are allowed to ride the rollercoasters")
time.sleep(5)
print("The height requirement for the roller coasters at the CodeU Amusement Park is 140 cm")
time.sleep(2)
print("Help them by building a code that will give them the answers they are looking for!")

heights = [208,200,137,141,127,145,134,250,190,133,127,201,206,142,147,115,187,178,170,175]
nbHeight = 0
nbPeople = len(heights)

for i in heights:
    if i >= 140:
        nbHeight += 1
print("The number of people signed up is " + str(nbPeople) + " and the number of people who can ride the rollercoasters is " + str(nbHeight))   


##     2) Exercise - How many letter 'a's are there - LEVEL EASY     ##
word = "abracadabra"
count = 0
for i in word:
    if i == "a":
        count += 1
print(count)

##     3) Exercise - How many a's are there - LEVEL MEDIUM
word = input("Please enter a word: ")
count = 0
for i in word:
    if i == "a":
        count += 1
print(count)

##     4) Exercise - How many letter 'a's are there - LEVEL HARD     ##
# Here, we are adding a second level of FOR loop. This is what we call a Nested Loop.
listWords = ["abracadabra", "algebra", "anaconda", "alakazam", "catamaran", "extravaganza"]
count = 0
for i in listWords:
    for j in i:
        if j == "a":
            count += 1
print(count)


##     5) Introduction Loop Controls: CONTINUE, BREAK, and PASS Statements     ## 

# Example 1: BREAK
for i in range(5):
    if i >= 3:
        break
    print(i)

# Example 2: You have to guess the correct answer
number = 5
while True:
    answer = int(input("Guess the correct number: "))
    if answer == number:
        break
print("That's the correct answer!")

# Example 3: CONTINUE
# You must print ALL the elements form the list of coding languages EXCEPT Python
languages = ["Java", "C#", "C++", "HTML", "Javascript", "Rust", "Perl"]
for i in languages:
    if i == "Python":
        continue
    else:
        print(i)


##     6) Final Exercise of the Day: Quick! Change my Report Card!     ##
print("Hi, my name is Alex, and I am currently failing most of my classes...")
time.sleep(2)
print("\nIf my mom finds out, she would kill me!")
time.sleep(2)
print("\nThe passing grade is 60, so I can't keep anything under that.")
time.sleep(2)
print("\nI need your help to update my report card and only keep the passing grades!")
time.sleep(2)
print("\nYou'll have to create a new list containing just the passing grades using CONTINUE!")

reportCard = [74, 59, 42, 66, 45, 85, 37, 47, 48, 63, 52, 16, 37, 28, 83, 95, 36, 62, 60, 60, 14]
newReportCard = []
for i in reportCard:
    if i < 60:
        continue
    else:
        newReportCard.append(i)
print("Here is your new report card!")
print(newReportCard)


####    HOMEWORK: Aliens?    ####

#   The CIA is currently investigation a HIGH SECRET case.
#   There is a remote island in the carribeans that they think is very suspicious.
#   Using satellites and radio, they're able to pick up weird and unusual signals.
#   They decide to send in a spy to scout the area and see what's going on.
#   As she explores the island, she spots a weird moving shape from the distance.
#   She gets closer and sees that it's...aliens!
#   As soon as she realizes, she runs away to hide while calling the CIA to let them know.
#   However, as she was running, she dropped the cellphone in a puddle.
#   She only able to let them know of the aliens, but not how many there were.
#   She remembered seeing a radio near where the aliens were stationed.
#   So, at night, she decided to infiltrate their camp to use their radio to communicate with the CIA.
#   Unfortunately, she could only communicate using different sequences of binary code (1101, 010, 0011, ...)
#   It's common knowledge at the CIA that all 1's represent an enemy. 

#   It is your duty to decrypt this message and determine how many aliens are present on the island!!

#   Here is the encrypted message received by the CIA
encryptedMessage = ["110010", "00000011", "10101", "111111110", "00110011010101010", "110100110110101", "110011100011110000"]


####    HOMEWORK CORRECTION    ####

# Set your alien counter
aliens = 0

# Build your code
for i in encryptedMessage:
    for j in i:
        if j == "1":
            aliens += 1

# Print a message containing the number of aliens on the island!
print("There are currently " + str(aliens) + " on the island!!")

