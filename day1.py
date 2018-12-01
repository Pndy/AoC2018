import csv

# Get puzzle input and make it into a list
with open('day1list.csv', 'r') as f:
    reader = csv.reader(f)
    input = list(reader)

frequency = 0
frequencyList = list()
iteration = 0

loop = True

# Function for looping thru the input values and acting as needed
def loopOverInput():
    global frequency
    global loop

    # Loop thru all of the input values and apply them to the frequency
    for i in range(len(input)):
        frequency = frequency + int(input[i][0])
        
        # if frequency is already in frequencyList
        # we can stop running the loop, print the frequency
        # that was first found a second time
        # Answer to part 2
        if frequency in frequencyList:
            loop = False
            print(frequency)
            return
        
        # Frequency not in the list yet, append it
        else:
            frequencyList.append(frequency)

# Run loopOverInput until 2 same frequencies have been met
while loop:
    iteration+=1
    
    # Print the frequency after first pass
    # Answer to part 1
    if iteration == 2: 
        print(frequency)
    loopOverInput()