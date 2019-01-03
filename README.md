# exaltered-nirvana-computing
Simple Python3 script for computing Nirvana values, used during the Naa'Maz Nirvana computations.

## Mathematical problem
Given a dice roll `ndk` (where `n` is the number of dice and `k` the sides for each die, e.g. `3d6` for a roll of `3` dice with `6` sides) and a probability `p`, we want to know the value `D` such that the sum of dice values is greater than `D` `p`% of the times.

The formulae used here were taken from https://www.lucamoroni.it/the-dice-roll-sum-problem/. Thank you Luca!

## Technical details

### Dependencies
This code runs on `Python3` with `numpy` and `scipy`. No other dependencies are required.

### Running
Run `python nirvana.py 3d6 50` to get the difficulty that a `3d6` roll passes 50% of the times.

You can also run `python nirvana.py 3d6 0.5` for the same answer.

By running `python nirvana.py` you'll get a raw list of the difficulties used in Exaltered for the Nirvana check for mages.
The implementation is rather quick and dirty as that was the main purpose of the program.

## Licensing
This code is licensed under MIT license.

## Contributing
Given the narrow scope of the implementation no further contribution should be required, if not for usability purposes or other success systems. If someone needs customisation for specific systems, they may open an issue or fork the repository themselves.
