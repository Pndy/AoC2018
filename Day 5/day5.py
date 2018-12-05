from array import array
import string

# Slow and unoptimized to what it could be
# takes a heck of a long time to run
# but eventually, producing the correct results :)

# Get puzzle input and make it into a list
input2 = open("day5input.txt").read()
input = list(input2)

finished = False

# Recursive function to remove the first instance
# of pattern "aA" / lowercase and uppercase next to eachother
# returns the string after removing it
# Toggles finished if no patterns matched
def d(inp):
    global finished
    for i in range(len(inp)):
        if i+1 == len(inp):
            finished = True
            return inp
        else:
            if inp[i].isupper() and inp[i+1].islower() or inp[i].islower() and inp[i+1].isupper():
                if inp[i].lower() == inp[i+1].lower():
                    del inp[i+1]
                    del inp[i]
                    return inp

# remove values from list function
def rmV(list, val):
    return [value for value in list if value  != val]

# Run recursive function until an answer has been found
while not finished:
    input = d(input)

# Answer to part 1
print("Answer to part 1: ",len(input))

start = len(input)
letters = list(string.ascii_lowercase)
uLetters = list(string.ascii_uppercase)
inputs = list()

# Repeats the proccess of part 1, running the same thing
# for each letter removed from the input
for i in range(len(letters)):
    newInput = list(input2)

    # Removes the current letters from input, both upper and lower
    newInput = rmV(newInput, letters[i])
    newInput = rmV(newInput, uLetters[i])
    finished = False

    # Again runs recursive function until answer has been found
    while not finished:
        newInput = d(newInput)
    inputs.append(len(newInput))

#Answer to part 2
print('Answer to part 2: ', min(inputs))