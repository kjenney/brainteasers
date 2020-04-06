from pprint import pprint
import argparse
from random import randint
from matchme import MatchMe

# Script to solve Brain Teasers

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', help='Common top-level parameter',
                    action='store_true', required=False)
subparsers = parser.add_subparsers(help='Clues to give', dest='clues')
parent_parser = argparse.ArgumentParser(add_help=False)

parent_parser.add_argument('-number', required=True,
                            help='the number posed as the example in the clue')
parent_parser.add_argument("-digits", required=True,
                            help="the number of digits to match in the clue")
parent_parser.add_argument("-validate", required=True,
                            help="is/are digit(s) right or wrong?",
                            choices=['valid','invalid'])
parent_parser.add_argument("-placement", required=True,
                            help="is/are the digit(s) in the correct or incorrect place?",
                            choices=['correct','incorrect'])

parser_create = subparsers.add_parser("--first", parents=[parent_parser],
                                      help='First clue')
parser_update = subparsers.add_parser("second", parents=[parent_parser],
                                      help='Second clue')
parser_update = subparsers.add_parser("third", parents=[parent_parser],
                                      help='Third clue')
parser_update = subparsers.add_parser("fourth", parents=[parent_parser],
                                      help='Fourth clue')
parser_update = subparsers.add_parser("fifth", parents=[parent_parser],
                                      help='Fifth clue')
args = parser.parse_args()

pprint(args.clues)
#first_matches = MatchMe(args)
