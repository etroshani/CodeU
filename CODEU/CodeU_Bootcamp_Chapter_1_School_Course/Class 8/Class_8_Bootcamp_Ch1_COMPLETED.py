##  Welcome to your 8th and final CODEU class!  ##


##   Recap of what was taught last class:   ## 
#       -JUMANJI Game


####    CODEU TOURNAMENT: ICE CREAM STORE    ####

#   You will build an ice-cream store where clients will walk in and be welcomed!
#   1) You must define a variable for the name of your store
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


##  WRITE YOURE CODE  ##
# Define your store name using INPUT() and welcome your guests to the store. Include your store name in the welcome message.
name = "CodeU's Ice Creams"
print("\nHi! Welcome to " + name)

# Define the flavor ice cream the customer wants using INPUT()
icecream = input("\nWhat flavor ice-cream would you like? vanilla | chocolate: ")

# Write the conditionals for ALL possible combinations
if icecream == "vanilla":
    # Define the size the customer wants using INPUT()
    size = input("What size cone would you like? small | medium | large: ")

    if size == "small":
        print("\nYour total will be 2$")
    elif size == "medium":
        print("\nYour total will be 5$")
    elif size == "large":
        print("\nSorry, we don't have enough vanill ice cream left for a large...")

elif icecream == "chocolate":
    # Define the size the customer wants using INPUT()
    size = input("What size cone would you like? small | medium | large: ")

    if size == "small":
        print("\nYour total will be 3$")
    elif size == "m":
        print("\nCongratulations! You are our 100th medium chocolate ice-cream ordered today! It's free!")
    elif size == "l":
        print("\nYour total will be 30$")
        
else:
    print("Sorry, we don't have that at " + name)

    
    
##      YOU HAVE NOW COMPLETED CHAPTER 1 OF THE CODEU BOOTCAMP!      ##
