class MatchMe:
    """Match a number against requirements"""
    def __init__(self, args):
        self.args = args
        self.number = args.first_clue_digits
        self.solve()

    def how_many_digits_to_match(self):
        return int(self.args.first_clue_context_digits)

    def how_many_digits_in_number(self):
        return len(self.number)

    def digits_boolean(self):
        """Is the digit there or not?"""
        if self.args.first_clue_context_boolean == 'right':
            return True
        else:
            return False

    def match_number_of_digits(self):
        print(self.how_many_digits_in_number())
        if self.digits_boolean:
            for i in range(0, self.how_many_digits_to_match()):
                print(i)

    def solve(self):
        self.match_number_of_digits()
        #if str(self.args.first_clue_digits)[0] in str(self.number):
        #    return True
        #else:
        #    return False

    def every_possible_match(self):
        """Start with an array of every number between 0 and 999* (* depends on the number of digits)"""
        list = []
        min = 0
        max = int('9' * number_of_digits) + 1 #include last number
        for i in range(0, max):
            list.append(str(i).zfill(number_of_digits))
        return list

    def another(self):

        print("Here is the teaser: Find a " + str(number_of_digits) + " digit number that matches the following requirements:")
        if int(args.first_clue_context_digits) > 1:
            context_digits_language = args.first_clue_context_digits + " digits that are "
        else:
            context_digits_language = args.first_clue_context_digits + " digit that is "
        print('\tThe number ' + args.first_clue_digits + ' has ' + context_digits_language + args.first_clue_context_boolean + ' and in the ' + args.first_clue_context_place + ' place')
