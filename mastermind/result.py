class Result():
    pass

class LostGame(Result):
    pass

class GuessResult(Result):
    def __init__(self, wellplaced, misplaced):
        self.wellplaced = wellplaced
        self.misplaced = misplaced

    def __eq__(self, other):
        return self.wellplaced == other.wellplaced and self.misplaced == other.misplaced