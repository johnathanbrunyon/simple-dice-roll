import random as rand

# Simple function to get the average of all rolls
def GetAverage(list):
    sum = 0
    for x in list:
        sum += x
    average = int(sum / len(list))
    print(average)

# Initializing the past rolls list
pastRolls = []

# User input
rollAmt = input("How many times do you want to roll a die? ")

i = 0

# Error checking for a string that cannot be cast into an integer
while i < 1:    
    try:
        rollAmt = int(rollAmt)
        i = 1
    except:
        print("Cannot convert an alpha-numeric string to an integer!")
        rollAmt = input("How many times do you want to roll a die? ")

# Generating a new roll, printing the new roll, and adding it to the list containing all previous rolls
iter = 0
while iter < rollAmt:
    currRoll = rand.randint(1, 6)
    print(currRoll)
    pastRolls.append(currRoll)
    iter += 1

# Printing average rolls
print("Average Roll")
GetAverage(pastRolls)