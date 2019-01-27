# exaltered-nirvana-computing
Simple Python3 script for computing the probabilities of outcome of a Rudra roll, forked from Nirvana.

## Mathematical problem
Given a dice roll `ndk` (where `n` is the number of dice and `k` the sides for each die, e.g. `3d6` for a roll of `3` dice with `6` sides), we want to know the distribution of the resulting Rudra roll.
The Rudra roll is different from both Nirvana rolls and standard White Wolf d10 rolls, in that the outcome is determined as follows:

"all die values shared by more than one die grant a number of success equal to the value itself"

For instance, a roll of [1, 1, 3, 3, 2] will give an outcome of 4, as the sum of 1 and 3 (the values that appear on more than one die).
A roll of [1, 3, 5, 4] will give an outcome of 0, since no values are shared between two or more dice.

## Technical details

### Dependencies
No dependencies on `numpy` or `scipy` is needed.

### Running
Run `python nirvana.py 3d6` to get the distribution of a `3d6` Rudra roll in decreasing order of probability.

## Licensing
This code is licensed under MIT license.
