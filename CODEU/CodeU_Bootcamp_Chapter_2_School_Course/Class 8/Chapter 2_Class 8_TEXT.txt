# Welcome to your 8th and final class of the CodeU Bootcamp Chapter 2! #


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
    
    elif action_taken == "throw" and computer == 3:
        if amount_of_balls >= 1:
            print("\nThe CodeU Robot has dodged your attack!")
            amount_of_balls -= 1
        else:
            print("\nYou have no balls to throw! You must pick-up at least one ball in order to throw it!")
            print("\nLuckily, no one has been hit!")
    
    elif action_taken == "pick-up" and computer == 1:
        print("\nWhile you were picking up a dodgeball, you were hit!")
        lives -= 1
        amount_of_balls += 1
    
    elif action_taken == "pick-up" and computer == 2:
        print("\nBoth parties have decided to pick up a ball so no one has been hit!")
        amount_of_balls += 1

    elif action_taken == "pick-up" and computer == 3:
        print("\nYou have picked up a ball and no one has been hit!")
        amount_of_balls += 1
    
    elif action_taken == "dodge" and computer == 1:
        print("\nYou dodged the CodeU robots throw!")

    elif action_taken == "dodge" and computer == 2:
        print("\nNo one has been hit!")

    elif action_taken == "dodge" and computer == 3:
        print("\nBoth parties dodged, so no one has been hit!")

# Final print of the attributes
print("\nYour lives: " + str(lives))
print("The CodeU robots lives: " + str(robot_lives))
print("Your amount of balls: " + str(amount_of_balls))

# Results once a Loop condition is filled
if lives == 0:
    print("\nThe CodeU Robot has won the game of CodeU dodgeball! \nBetter luck next time!")
elif lives == 0 and robot_lives == 0:
    print("\nYou both won the game as you eliminated each other at the same time!")
else: 
    print("\nCongratulations! You have officially won the game of CodeU Dodgeball!")
