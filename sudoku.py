from math import sqrt

IDEA_LIST = list(range(1, 5))
IDEA_LEN = len(IDEA_LIST)
IDEA_SQR = int(sqrt(IDEA_LEN))


class SudokuLine(object):
    def __init__(self, line_contents):
        self.valid = False
        self.line_contents = line_contents
        self.validate()

    def validate(self, _contents=None):
        contents = self.line_contents if _contents is None else _contents
        assert len(contents) == len(IDEA_LIST)
        seen = []
        for item in contents:
            if item not in seen and item is not None:
                seen.append(item)
            elif item is not None:
                raise ValueError("Valor repetido")

    def check_valid(self):
        self.valid = None not in self.line_contents

    def get_possibilities(self, _contents=None):
        contents = self.line_contents if _contents is None else _contents
        missing_no = set(IDEA_LIST) - set(contents)
        return {indx: list(missing_no) for indx in [i for (i, val)
                in enumerate(contents) if val is None]}


class SudokuSquare(SudokuLine):
    def __init__(self, square_contents):
        self.valid = False
        self.square_contents = square_contents
        self.validate()

    def validate(self, _contents=None):
        super(SudokuSquare, self).validate(
            [item for sublist in self.square_contents for item in sublist])

    def get_possibilities(self, _contents=None):
        return super(SudokuSquare, self).get_possibilities(
            [item for sublist in self.square_contents for item in sublist])


class SudokuGame(object):
    def __init__(self, game):
        self.valid = False
        self.rows = game
        self.cols = [[sl[i] for sl in game] for i in range(len(game))]
        flat_list = [item for sublist in game for item in sublist]
        chunks = [flat_list[i:i + IDEA_SQR]
                  for i in range(0, len(flat_list), IDEA_SQR)]
        self.squares = [[chunks[i]] + [chunks[i + IDEA_SQR]]
                        for i in range(len(chunks) - IDEA_SQR)]

    def print_game(self):
        print ""
        upper_line = ""
        for i in range((len(IDEA_LIST) + IDEA_SQR) + 1):
            upper_line += "-"
        print upper_line
        line_str = "|"
        for i in range(IDEA_SQR):
            line_str += ("{}" * IDEA_SQR) + "|"
        for i in range(IDEA_LEN):
            print line_str.format(*[val if val is not None else '@' for val in self.rows[i]])
            if (i + 1) % IDEA_SQR == 0:
                print upper_line


def main():
    """
    col1 = SudokuLine([1, 2, 3, None, 5, 6, 7, 9, None])
    print col1.get_possibilities()
    sqr = SudokuSquare([[None, 2, 1], [3, None, 4], [6, 7, 8]])
    print sqr.get_possibilities()
    """
    jogo = [[2, 4 , 7, 8], [None , 3, 6, 5], [9, 8, 7, 6], [3, 1, 2, 6]]
    new = SudokuGame(jogo)
    new.print_game()


if __name__ == "__main__":
    main()
main()
