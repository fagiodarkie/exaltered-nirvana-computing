import sys
import numpy
from scipy.special import binom

def help():
    print("Usage: python nirvana.py NdK P")
    print("\tN: number of dice, e.g. 3")
    print("\tK: number of sides for each die, e.g. 6")
    print("\tP: probability of success, e.g. 15")

def computeArguments():
    [die, sides] = sys.argv[1].split("d")
    prob = sys.argv[2]
    return (die, sides, prob)

def computeProbability(die, sides, prob):
    return "probability"

if __name__ == "__main__":
    if (len(sys.argv)) != 3:
        help()
        exit()
    (die, sides, probability) = computeArguments()

    print(computeProbability(die, sides, probability))

