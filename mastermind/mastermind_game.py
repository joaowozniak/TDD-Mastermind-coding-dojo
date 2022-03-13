from mastermind.evaluator import MastermindGuessEvaluator
from mastermind.result import *

class MastermindGame:
    def __init__(self, attempts = 0):
        self.result = Result()
        self.mastermindGuessEvaluator = MastermindGuessEvaluator()
        self.attempts = attempts        

    def guess(self, secret: list, guess: list) -> Result:
        if self.attempts >= 10:
            return LostGame()

        self.attempts += 1
        return self.mastermindGuessEvaluator.evaluate(secret, guess)

