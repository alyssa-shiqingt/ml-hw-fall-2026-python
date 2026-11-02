class InputNumbers:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def find(self, x):
        for i in range(len(self.numbers)):
            if self.numbers[i] == x:
                return i + 1
        return -1