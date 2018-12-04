
# UNFINISHED SPAGETTI CODE AHEAD
# for some reason, i never got part 1 working here,
# as i guess theres something wrong at some point
# but part 2 was easy, altho even to that i had to do some manual work

# would advice you to not touch this

# TODO 
# fix this mess


import re
import datetime

# Get puzzle input and make it into a list
input = open("day4input.txt").read().splitlines()

inp = list()
for line in input:
    p = re.split('] ', line)
    inp.append({'timestamp':p[0]+']', 'value':p[1]})

# Sort the list with timestamp
inp.sort(key=lambda x:datetime.datetime.strptime(x['timestamp'], '[%Y-%m-%d %H:%M]'))

sleeping = False
currGuard = ""
sleepSchedule = ""

listt = list()

for l in inp:
    v = l['value']
    t = l['timestamp']
    m = re.split(' ', t)
    m = re.split(':', m[1])
    m = int(m[1].replace(']',''))
    # Guard change
    if v.startswith('Guard'):
        g = re.split(' ', v)
        g = g[1]
        if sleeping:
            for n in range(59-len(sleepSchedule)):
                sleepSchedule += "#"
        else:
            for n in range(59-len(sleepSchedule)):
                sleepSchedule += "."
        app = '{0} - {1}'.format(sleepSchedule, currGuard)
        listt.append(app)
        #print(sleepSchedule , " | ", currGuard)
        currGuard=g
        sleepSchedule=""
        sleeping = False

    # Starts sleeping
    if v.startswith('falls'):
        sleeping = True
        for n in range(m-len(sleepSchedule)):
            sleepSchedule += "."
    if v.startswith('wakes'):
        sleeping = False
        for n in range(m-len(sleepSchedule)):
            sleepSchedule += "#"

guardList = list()
guardList.append("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  - #0")
found = False
for line in listt:
    parsedd = re.split(' - ', line)
    for line2 in guardList:
        parsed = re.split(' - ', line2)
        #print(parsedd[1], ' - ', parsed[1])
        if parsed[1] == parsedd[1]:
            guardListItemI = guardList.index(line2)
            guardListItem = guardList.pop(guardListItemI)
            itemParsed = re.split(' - ', guardListItem)
            item2Parsed = itemParsed[0].split()
            #print(item2Parsed)
            newString = ""
            for i in range(58):
                num = int(item2Parsed[i])
                if parsedd[0][i] == "#":
                    newString += str(num+1)
                else:
                    newString += str(num)
                newString += " "
            app = '{0} - {1}'.format(newString, itemParsed[1])
            guardList.append(app)
            found = True
    if not found:
        string = ""
        for i in parsedd[0]:
            if i == ".":
                string += '0'
            if i == "#":
                string += '1'
            string+=" "
        app = '{0} - {1}'.format(string, parsedd[1])
        guardList.append(app)
        found=False
    else:
        found=False

total = list()
most = list()
for line in guardList:
    par = line.split(' - ')
    nums = par[0].split()
    totalN = 0
    mostN = 0
    for num in nums:
        totalN += int(num)
        if num != "0"w:
            mostN += 1
    app = "{0} {1} {2}".format(totalN,mostN,par[1])
    total.append(app)

for line in total:
    print(line)