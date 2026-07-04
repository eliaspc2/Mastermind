import random

class RandomOrder:
    """Responsável por gerar a ordem dos números aleatórios."""

    def __init__(self, numbers = 4):
        self.numbers = numbers

    def shuffle(self):
        return [random.randint(0, 10) for i in range (self.numbers)]

