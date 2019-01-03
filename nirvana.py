import sys
import numpy
from scipy.special import binom

def help():
    print("Usage: python nirvana.py NdK P")
    print("\tN: number of dice, e.g. 3")
    print("\tK: number of sides for each die, e.g. 6")
    print("\tP: probability of success, e.g. 15")

def computeArguments(arg):
    [die, sides] = arg[1].split("d")
    prob = arg[2]
    return (int(die), int(sides), int(prob))

def signedK(dieNumber, dieSides, s):
    return int(numpy.floor((s - dieNumber) / dieSides))

def specialSum(n, k, s):
    accumulator = 0
    signedk = signedK(n, k, s)
    for j in range(signedk + 1):
        partial = ((-1)**j) * binom(n, j) * binom(s - k*j - 1, s - k*j - n)
        accumulator += partial
    return accumulator

def computeDifficulty(die, sides, prob):
    if prob >= 1:
        prob /= 100
    difficulty = die * sides
    currentProbability = 0
    while (currentProbability < prob) & (difficulty > 1):
        probToRollDiff = (1 / (sides ** die)) * specialSum(die, sides, difficulty)
        currentProbability += probToRollDiff
        difficulty -= 1
    return difficulty

if __name__ == "__main__":

    if (len(sys.argv)) == 1:
        for die in ["1d2", "2d4", "3d6", "4d8", "5d12", "6d24", "7d30", "8d60", "9d100"]:
            for P in ["1", "15", "55", "60", "70", "80", "85", "90", "95", "97", "99"]:
                (d, side) = die.split("d")
                if (int(d) > 5) and (P == "55"):
                    print(die, "30", computeDifficulty(int(d), int(side), 30))
                else:
                    print(die, P, computeDifficulty(int(d), int(side), int(P)))
        exit()

    if (len(sys.argv)) != 3:
        help()
        exit()
    (die, sides, probability) = computeArguments(sys.argv)
    print(computeDifficulty(die, sides, probability))

