#Welcome to your 7th CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own.


## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


#   In the 7th class, we are covering these topics:
#       Project: CodeU Dodgeball Game!



####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       Loops: FOR
#       Loop controls: CONTINUE and BREAK statements


##   REVIEW HOMEWORK   ##
# Review the homework to correct any mistake they may have done or to answer any question they may have.



####    SECOND PART    ####

##     CodeU Dodeball Game!     ##
import random
import time

print("\nWelcome to a game of CodeU Dodgeball!")
time.sleep(2)
print("\nYou are faced with the infamous CodeU Robot at a game of Dodgeball...")
time.sleep(3)
print("\nThe Robot, being a master of dodgeball, unfortunately has an advantage where it can generate a ball at anytime without having to pick it up.")
time.sleep(4)
print("\nLuckily for you, the Robot has an issue...")
time.sleep(2)
print("\nIt sometimes has a completely RANDOM malfunction where it cannot move...")
time.sleep(2)
print("\nOtherwise, it can either shoot a ball or dodge. Any action from the Code Robot is done randomly.")
time.sleep(3)
print("\nThis makes it completely unpredictable...")
time.sleep(2)
print("\nYou, on the other hand, can either shoot a dodgeball, pick-up a dodgeball, or dodge an attack.")
time.sleep(3)
print("\nUnfortunately, you are unable to shoot if you haven't picked up at least one dodgeball!")
time.sleep(3)
print("\nConsidering the robot is a master at dodgeball, it'll only have 3 lives, whereas you will have 5.")
time.sleep(3)
print("\nYou start the game with NO balls in your possession!")
time.sleep(3)
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