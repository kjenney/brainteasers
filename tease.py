from pprint import pprint
import argparse
from random import randint

# Script to solve Brain Teasers

class MatchMe:
    """Match a number against requirements"""
    def __init__(self, number, args):
        self.number = number
        self.args = args
        self.solve()

    def how_many_digits_to_match(self):
        return int(self.args.first_clue_context_digits)

    def digits_boolean(self):
        """Is the digit there or not?"""
        if self.args.first_clue_context_boolean == 'right':
            return True
        else:
            return False

    def match_number_of_digits(self):
        if self.digits_boolean:
            for i in range(0, self.how_many_digits_to_match()):
                print(i)

    def solve(self):
        self.match_number_of_digits()
        #if str(self.args.first_clue_digits)[0] in str(self.number):
        #    return True
        #else:
        #    return False

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

# Generate random numbers of number_of_digits in length until 1 matches the requirement
min = 0
max = int('9' * number_of_digits)
while True:
    matched = False
    digits = [str(randint(min, max)) for i in range(5)]
    for digit in digits:
        number = (len(str(max))-len(digit))*'0'+digit
        MatchMe(number, args)
        break
        #if matched:
        #    print(number)
        #    break
    #if matched:
    break
