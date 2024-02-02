# Welcome to your 6th class! #


####    FIRST PART    ####

# Recap of Class 5 theory: 
#       Loops: FOR
     

###     HOMEWORK SOLUTION     ###

# Build the list of tourists
weight = [208, 200, 350, 500, 127, 145, 134, 900]

# Number of tourists
participants = len(weight)

# Create the variable where you will be adding the weight of every person
weight_total = 0

# Create the FOR Loop
for i in weight:
    weight_total += i

# Print the results
print(str(participants) + " participants weigh a total of " + str(weight_total))




####    SECOND PART    ####


##     1) First Exercise Of The Day - CodeU Amusement Park      ##

# Build your list of heights
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



##     3) Exercise - How many letter 'a's are there - LEVEL HARD     ##
# Here, we are adding a second level of FOR loop. This is what we call a Nested Loop.
listWords = ["abracadabra", "algebra", "anaconda", "alakazam", "catamaran", "extravaganza"]
count = 0
for i in listWords:
    for j in i:
        if j == "a":
            count += 1
print(count)



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


####    CODE HERE    ####



