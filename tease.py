from pprint import pprint
import argparse
from random import randint
from matchme import MatchMe

# Script to solve Brain Teasers

parser = argparse.ArgumentParser(description='Solve a brain teaser.')
parser.add_argument('-c', '--clue', action='append', nargs=4,
    metavar=('number','digits','validity','placement'), help='help:', required=True)
args = parser.parse_args()

if args:
    MatchMe(args)
else:
    print('Clues are required')

# w = {1,2,3,4,5,6,7}
# x = {4,5,6,7,8,9,10}
# y = {7,8,9,10,11,12,13}
# ranges = [w,x,y]
# ranges_to_compare = ranges.copy()
# ranges_to_compare.pop(0)
#
# z = ranges[0].intersection(*ranges_to_compare)

# print(z)
