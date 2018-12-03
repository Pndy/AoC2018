import re

# Get puzzle input and make it into a list
input = open("day3input.txt").read().splitlines()

# Create 2 grids, one for part 1 and another for part 2
# and 2 sets, to filter for part 2
grid = [[0] * 1000 for h in range(1000)]
grid2 = [[None] * 1000 for h in range(1000)]
all = set()
blacklist = set()

part1 = 0


for line in input:
    # Parse "#1 @ 1,3: 4x4" into readable format
    parsed = re.split(' @ |,|: |x', line)
    x = int(parsed[1])
    y = int(parsed[2])
    w = int(parsed[3])
    h = int(parsed[4])
    all.add(parsed[0])

    for i in range(w):
        for j in range(h):
            # Add to the current cell, and if the cell is
            # 2 then add to the total overlapping
            grid[x+i][y+j] += 1
            if grid[x+i][y+j] == 2:
                part1 +=1

            # if the current cell is empty, add ID to it
            # but if there is already id in it, blacklist
            # the id in the cell and the id thats trying to claim
            # the cell, as they are overlapping
            if grid2[x+i][y+j] is None:
                grid2[x+i][y+j] = parsed[0]
            else:
                blacklist.add(grid2[x+i][y+j])
                blacklist.add(parsed[0])

# Answers to part 1 and 2
print("Part 1:", part1)
print("Part 2: ", all - blacklist)