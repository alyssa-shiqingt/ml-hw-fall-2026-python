# Read N
print('type N')
N = int(input())

# Read all N numbers one by one
print('type ', N, 'numbers, one by one.')
numbers = []
for i in range(1, N + 1):
    print('type #', i, 'number:')
    numbers.append(int(input()))

# Read X
print('type X')
X = int(input())

# Output decision if X is part of the N input numbers
if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)