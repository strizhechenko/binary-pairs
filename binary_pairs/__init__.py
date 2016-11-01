from metacomm.combinatorics.all_pairs2 import all_pairs2 as all_pairs


class BinaryPairs(object):

    def __init__(self, number):
        parameters = [[0, 1]] * number
        self.pairs = all_pairs(parameters)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.pairs])
