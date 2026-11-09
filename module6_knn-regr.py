import numpy as np

class KNN:
    def __init__(self,  n, k):
        # Training set
        self.points = np.empty((0, 2), dtype=float)
        # How many points in training
        self.n = n
        # How many neighbors
        self.k = k

        if self.k > self.n or self.k <= 0:
            raise ValueError(f"Invalid k: must be between 1 and N. But got k = {self.k} and N = {self.n}")

    def insert(self, x, y):
        self.points = np.vstack((self.points, [x, y]))

    def predict(self, x):
        if self.points.shape[0] < self.n:
            raise ValueError(f"Not enough points to predict: need {self.n} points, but only got {self.points.shape[0]}")

        distances = np.abs(self.points[:, 0] - x)
        # Find the indices of the k NN
        nearest_indices = np.argsort(distances)[:self.k]
        # Calculate the mean of Y values
        return np.mean(self.points[nearest_indices, 1])

def main():
    n = int(input("input N (positive integer): "))
    k = int(input("input k (positive integer): "))

    knn = KNN(n = n, k = k)

    for i in range(1, n + 1):
        print(f"input point {i} of {n}:")
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        knn.insert(x, y)

    x = float(input("input X for prediction now: "))

    try:
        y = knn.predict(x)
        print(f"Predicted Y: {y}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()