from pprint import pprint
import argparse
from random import randint
from matchme import MatchMe

# Script to solve Brain Teasers

parser = argparse.ArgumentParser(description='Solve a brain teaser.')
parser.add_argument("--first", help="a comma separated value of the clue", required=True)
parser.add_argument("--second", help="a comma separated value of the clue", required=False)
parser.add_argument("--third", help="a comma separated value of the clue", required=False)
parser.add_argument("--fourth", help="a comma separated value of the clue", required=False)
parser.add_argument("--fifth", help="a comma separated value of the clue", required=False)
args = parser.parse_args()

MatchMe(args)
