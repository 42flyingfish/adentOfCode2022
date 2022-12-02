def processFile():
    with open('input.txt') as stuff:
        total = 0;
        for line in stuff:
            if line == '\n':
                yield total
                total = 0;
            else:
                total = total + int(line)


def getMostCalories():
    return max(x for x in processFile())


def getTopNCalories(n):
    groupings = [x for x in processFile()]
    groupings.sort(reverse=True) # Sort by largest
    for i in range(n):
        yield groupings[i]


print(f'The highest Calorie Count is {getMostCalories()}')
print(f'The total of the top 3 is {sum(getTopNCalories(3))}')
