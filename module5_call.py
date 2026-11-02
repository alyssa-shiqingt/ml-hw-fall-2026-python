from module5_mod import InputNumbers

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