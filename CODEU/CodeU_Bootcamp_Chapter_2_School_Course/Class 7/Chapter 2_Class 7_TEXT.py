# Welcome to your 7th class! #

####    FIRST PART    ####

# Recap of Class 6 theory and previous theory: 
#       FOR Loops  
#       While Loops


###     HOMEWORK SOLUTION     ###

encryptedMessage = ["110010", "00000011", "10101", "111111110", "00110011010101010", "110100110110101", "110011100011110000"]

# Set your alien counter
aliens = 0

# Build your code
for i in encryptedMessage:
    for j in i:
        if j == "1":
            aliens += 1

# Print a message containing the number of aliens on the island!
print("There are currently " + str(aliens) + " on the island!!")




####    SECOND PART    ####

##     CodeU Dodeball Game!     ##
import random
import time

print("\nWelcome to a game of CodeU Dodgeball!")
time.sleep(2)
print("\nYou must do your best to defeat the CodeU Robot and become the champion...")
time.sleep(3)
print("\nGood luck!")


# Set your Attributes
lives = 5
robot_lives = 3
amount_of_balls = 0

# Build your code
while lives > 0 and robot_lives > 0:

    # Printing the updated Attributes
    print("\nYour lives: " + str(lives))
    print("The CodeU robots lives: " + str(robot_lives))
    print("Your amount of balls: " + str(amount_of_balls))

    # Your actions
    action_taken = input("\nPick an action: Throw, pick-up or dodge: ")
    
    # CodeU Robot's actions: 1 -> Throws a ball, 2 -> Malfunctions, 3 -> Dodges
    computer = random.randrange(1,3)

    # Code ALL the different scenarios
    if action_taken == "throw" and computer == 1:
        if amount_of_balls >= 1:
            print("\nYou have been hit!")
            print("\nYou've struck the CodeU robot!")
            lives -= 1
            robot_lives -= 1
            amount_of_balls -= 1
        else:
            print("\nYou have no balls to throw! You must pick-up at least one ball in order to throw it!")
            print("\nYou've been hit!")
            lives -= 1

    elif action_taken == "throw" and computer == 2:
        if amount_of_balls >= 1:
            print("\nYou've struck the CodeU robot while it was malfunctioning!")
            robot_lives -= 1
            amount_of_balls -= 1
        else:
            print("\nYou have no balls to throw! You must pick-up at least one ball in order to throw it!")
            print("\nLuckily, the robot was malfunctioning so no one has been hit!")
