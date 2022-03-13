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
                if secret[idx] not in secretColours:
                    secretColours[secret[idx]] = 1
                else: 
                    secretColours[secret[idx]] += 1

                if guess[idx] not in misplacedColours:                    
                    misplacedColours[guess[idx]] = 1
                else: 
                    misplacedColours[guess[idx]] += 1

        misplaced = self.__count_misplaced(misplacedColours, secretColours)            
     
        return GuessResult(wellplaced, misplaced)   

    def __count_misplaced(self, misplacedColours: dict, secretColours:dict) -> int:
        misplaced = 0

        for colour, count in misplacedColours.items():
            if colour in secretColours.keys():
                misplaced += count

        return misplaced
