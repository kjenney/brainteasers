from pprint import pprint
import argparse
from random import randint
from matchme import MatchMe

# Script to solve Brain Teasers

parser = argparse.ArgumentParser(description='Solve a brain teaser.')
parser.add_argument('-c', '--clue', action='append', nargs=4,
    metavar=('number','digits','validity','placement'), help='help:', required=True)
args = parser.parse_args()

Archimedes(args)
