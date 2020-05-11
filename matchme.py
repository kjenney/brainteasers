from pprint import pprint

class Archimedes:
    """The amazing Archimedes. Solve any Brain Teaser instantly!"""
    def __init__(self, args):
        self.args = args
        self.solve()

    def solve(self):
        print('Solving for it')
        # 2. Process each clue and return a collection of sets
        collection_of_sets = self.process_clues()
        # 3. Compare the first set with the rest to get the answer
        ranges_to_compare = collection_of_sets.copy()
        ranges_to_compare.pop(0)
        print(collection_of_sets[0].intersection(*ranges_to_compare))

    def process_clues(self):
        """Returns a collection of sets - one from each clue"""
        collection_of_sets = []
        for clue in self.args.clue:
            collection_of_sets.append(self.process_clue(clue))
        return collection_of_sets

    def process_clue(self, clue):
        number, digits, validate, placement = self.extract_clue(clue)
        # If the clue is asking for an exact match - return it
        if int(digits) == self.how_many_digits_in_number(number) and validate == 'valid':
            return number
        # Otherwise iterate over every possible number
        else:
            matches = self.match_clue(number, self.every_possible_match(number), validate, placement)
            pprint(matches)
            return matches

    def extract_clue(self, clue):
        number = clue[0]
        digits = clue[1]
        validate = clue[2]
        placement = clue[3]
        return number, digits, validate, placement

    def match_clue(self, number, rangeofnumbers, validate, placement):
        """Returns a set that is the range of numbers that solve for a clue"""
        matches = {}
        for i in rangeofnumbers:
            matches.add(i)
        return matches

    def every_possible_match(self, number):
        """Start with an array of every number between 0 and 999* (* depends on the number of digits)"""
        every = []
        min = 0
        max = int('9' * self.how_many_digits_in_number(number)) + 1 #include last number
        for i in range(0, max):
            every.append(str(i).zfill(self.how_many_digits_in_number(number)))
        return every
    #
    # def test_this(self, number, rangeofnumbers, validate, placement):
    #     matches = []
    #     number = 682
    #     another_number = 882
    #     asplat = self.split(str(number))
    #     bsplat = self.split(str(another_number))
    #     #digits = self.how_many_digits_in_number(number) - 1
    #     digits = 3
    #     pprint(range(3))
    #     #print(digits)
    #     #pprint(range(digits))
    #     #for n in range(0,100):
    #     #    print(n)
    #         #if asplat[i] == bsplat[i]:
    #         #    matches.append(another_number)
    #     return matches
    #
    #     # matches = []
    #     # number = 682
    #     # if validate == "valid" and placement == "correct":
    #     #     for i in range:
    #     #         for j in self.split(str(number)):
    #     #             if j in str(i):
    #     #                 matches.append(i)
    #     # return matches
    #
    # def split(self, word):
    #     return [char for char in word]
    #
    # def how_many_digits_in_number(self, number):
    #     return len(str(number))
    # #
    # # def digits_boolean(self):
    # #     """Is the digit there or not?"""
    # #     if self.args.first_clue_context_boolean == 'right':
    # #         return True
    # #     else:
    # #         return False
    # #
    # # def match_number_of_digits(self):
    # #     print(self.how_many_digits_in_number())
    # #     if self.digits_boolean:
    # #         for i in range(0, self.how_many_digits_to_match()):
    # #             print(i)
    # #
    # # def solve(self):
    # #     self.match_number_of_digits()
    # #     #if str(self.args.first_clue_digits)[0] in str(self.number):
    # #     #    return True
    # #     #else:
    # #     #    return False
    # #
    #
    # def another(self):
    #
    #     print("Here is the teaser: Find a " + str(number_of_digits) + " digit number that matches the following requirements:")
    #     if int(args.first_clue_context_digits) > 1:
    #         context_digits_language = args.first_clue_context_digits + " digits that are "
    #     else:
    #         context_digits_language = args.first_clue_context_digits + " digit that is "
    #     print('\tThe number ' + args.first_clue_digits + ' has ' + context_digits_language + args.first_clue_context_boolean + ' and in the ' + args.first_clue_context_place + ' place')
