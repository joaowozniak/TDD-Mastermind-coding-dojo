from mastermind.result import *

class MastermindGuessEvaluator:
    def __init__(self):
        pass

    def evaluate(self, secret: list, guess: list) -> GuessResult:
        wellplaced = 0
        secretColours = {}
        misplacedColours = {}

        for idx in range(len(guess)):
            if secret[idx] == guess[idx]:
                wellplaced += 1
            else:
                secretColours.setdefault(secret[idx], 1)                
                secretColours[secret[idx]] += 1
                misplacedColours.setdefault(guess[idx], 0)
                misplacedColours[guess[idx]] += 1
                        
        return GuessResult(wellplaced, self.__count_misplaced(misplacedColours, secretColours))   

    def __count_misplaced(self, misplacedColours: dict, secretColours:dict) -> int:
        misplaced = 0

        for colour, count in misplacedColours.items():
            if colour in secretColours.keys():
                misplaced += count

        return misplaced
