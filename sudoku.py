IDEA_LIST = list(range(1, 10))


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


def main():
    col1 = SudokuLine([1, 2, 3, None, 5, 6, 7, 9, None])
    print col1.get_possibilities()
    sqr = SudokuSquare([[None, 2, 1], [3, None, 4], [6, 7, 8]])
    print sqr.get_possibilities()

if __name__ == "__main__":
    main()

main()
