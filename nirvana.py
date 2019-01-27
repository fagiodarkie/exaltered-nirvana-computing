import sys
import operator

def help():
    print("Usage: python nirvana.py NdK P")
    print("\tN: number of dice, e.g. 3")
    print("\tK: number of sides for each die, e.g. 6")

def computeArguments(arg):
    [die, sides] = arg[1].split("d")
    return (int(die), int(sides))

def checkSuccess(rolledDice, possibleResults):
    resultDice = {}
    rollResult = 0
    for die in rolledDice:
        if die not in resultDice:
            resultDice[die] = 1
        else:
            resultDice[die] += 1

    for dieVal in resultDice:
        if resultDice[dieVal] > 1:
            rollResult += dieVal

    if rollResult not in possibleResults:
        possibleResults[rollResult] = 1
    else:
        possibleResults[rollResult] += 1

def getResults(rolledDice, dieNumber, sides, possibleResults):
    if dieNumber > 0:
        for result in range(1, sides + 1):
            getResults(rolledDice + [result], dieNumber - 1, sides, possibleResults)
    else:
        checkSuccess(rolledDice, possibleResults)

def computeDifficulty(die, sides):
    possibleResults = {}
    rolledDice = []
    getResults(rolledDice, die, sides, possibleResults)

    totalRolls = sides ** die

    sortedResults = dict(sorted(possibleResults.items(), key=lambda kv : -kv[1]))

    for result in sortedResults:
        sortedResults[result] = str((sortedResults[result] / totalRolls) * 100) + "%"


    return sortedResults

if __name__ == "__main__":

    if (len(sys.argv)) != 2:
        help()
        exit()
    (die, sides) = computeArguments(sys.argv)
    if die < 1:
        print("Wrong number of dice selected")
        exit()

    print(computeDifficulty(die, sides))

