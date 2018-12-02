# Get puzzle input and make it into a list
input = open("day2input.txt").read().splitlines()

twice = 0
thrice = 0

# loop thru each word in input
for word in input:
    twiceFound = False
    thriceFound = False

    # Builds array that shows how many times each letter is found
    # and toggles either to to true if one is found
    found = [[x,word.count(x)] for x in set(word)]
    for elem in found:
        if elem[1] == 2 and twiceFound == False:
            twiceFound = True
        if elem[1] == 3 and thriceFound == False:
            thriceFound = True

    # Adds to the total amounts if either is true
    if twiceFound:
        twice += 1
    if thriceFound:
        thrice += 1

# Answer to part 1
print("Part 1:",twice * thrice)

mostCorrect = 10
mostCorrectWord = ""
mostCorrectWord2 = ""

# Loops thru every word in input,
# Then does a second loop to compare them
for word in input:
    for test in input:
        fails = 0
        # loops for the words amount comparing each letter
        # and adding to fails if they dont match
        for i in range(len(word)):
            if word[i] != test[i]:
                fails+=1
        
        # If the fail amount if this run is lower than
        # the best run yet, correct the best run
        # Skips if no fails are found as it has
        # compared to itself, slighly inefficient
        if fails < mostCorrect and fails != 0:
            mostCorrect = fails
            mostCorrectWord = word
            mostCorrectWord2 = test

# Build the answer
answer = ""
for i in range(len(mostCorrectWord)):
    if mostCorrectWord[i] == mostCorrectWord2[i]:
        answer+=mostCorrectWord[i]

# Answer to Part 2
print("Part 2:",answer)