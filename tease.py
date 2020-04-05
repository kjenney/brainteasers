from pprint import pprint
import argparse

# Script to solve Brain Teasers

parser = argparse.ArgumentParser()
parser.add_argument("--first_clue_digits", help="first clue digits", required=True)
parser.add_argument("--first_clue_context_digits", help="the number of digits to match", required=True)
parser.add_argument("--first_clue_context_boolean", help="is/are digits right or wrong?", choices=['right', 'wrong'], required=True)
parser.add_argument("--first_clue_context_place", help="is/are the digit(s) in the correct or incorrect place?", choices=['correct', 'incorrect'], required=True)
args = parser.parse_args()

number_of_digits = len(args.first_clue_digits)
print("Here is the teaser: Find a " + str(number_of_digits) + " digit number that matches the following requirements:")
if int(args.first_clue_context_digits) > 1:
    context_digits_language = args.first_clue_context_digits + " digits that are "
else:
    context_digits_language = args.first_clue_context_digits + " digit that is "
print('\tThe number ' + args.first_clue_digits + ' has ' + context_digits_language + args.first_clue_context_boolean + ' and in the ' + args.first_clue_context_place + ' place')
