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


def main():
    # Read N
    n = int(input(f"Enter N: "))

    numbers = InputNumbers()
    for i in range(1, n + 1):
        number = int(input(f"Enter number {i}: "))
        numbers.insert(number)

    x = int(input("Enter X: "))

    print(numbers.find(x))


if __name__ == "__main__":
    main()