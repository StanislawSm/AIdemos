import numpy as np

class Node:
    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.feature_idx = None
        self.feature_value = None
        self.node_prediction = None


    def gini_best_score(self, y, possibleSplits):
        best_gain = -np.inf
        best_idx = 0

        # From here starts mine code implementing formulas written by teacher on whiteboard

        for split in possibleSplits:
            topOnes = np.sum(y[0:split])
            topZeros = y[0:split].size - topOnes
            bottomOnes = np.sum(y[split:-1])
            bottomZeros = y[split:-1].size - bottomOnes

            PtopOne = (topOnes / (topOnes + topZeros))**2
            PtopZero = (topZeros / (topOnes + topZeros))**2
            Itop = 1 - PtopOne - PtopZero

            PbottomOne = (bottomOnes / (bottomOnes + bottomZeros))**2
            PbottomZero = (bottomZeros / (bottomOnes + bottomZeros))**2
            Ibottom = 1 - PbottomOne - PbottomZero

            T = len(y[0:split])
            B = len(y[split:-1])
            N = T + B

            gain = 1 - (T/N * Itop + B/N * Ibottom)

            if gain > best_gain:
                best_gain = gain
                best_idx = split

        # end of mine code

        return best_idx, best_gain

    def split_data(self, X, y, idx, val):
        left_mask = X[:, idx] < val
        return (X[left_mask], y[left_mask]), (X[~left_mask], y[~left_mask])

    def find_possible_splits(self, data):
        possible_split_points = []
        for idx in range(data.shape[0] - 1):
            if data[idx] != data[idx + 1]:
                possible_split_points.append(idx)
        return possible_split_points

    def find_best_split(self, X, y):
        best_gain = -np.inf
        best_split = None

        for d in range(X.shape[1]):
            order = np.argsort(X[:, d])
            y_sorted = y[order]
            possible_splits = self.find_possible_splits(X[order, d])
            idx, value = self.gini_best_score(y_sorted, possible_splits)
            if value > best_gain:
                best_gain = value
                best_split = (d, [idx, idx + 1])

        if best_split is None:
            return None, None

        best_value = np.mean(X[best_split[1], best_split[0]])

        return best_split[0], best_value

    def predict(self, x):
        if self.feature_idx is None:
            return self.node_prediction
        if x[self.feature_idx] < self.feature_value:

            # mine changes
            if self.left_child is None:
                return self.node_prediction
            # mine changes end
            return self.left_child.predict(x)
        else:
            # mine changes
            if self.right_child is None:
                return self.node_prediction
            # mine changes end
            return self.right_child.predict(x)

    def train(self, X, y, depth):
        self.node_prediction = np.mean(y)
        if X.shape[0] == 1 or self.node_prediction == 0 or self.node_prediction == 1:
            return True

        self.feature_idx, self.feature_value = self.find_best_split(X, y)
        if self.feature_idx is None:
            return True

        (X_left, y_left), (X_right, y_right) = self.split_data(X, y, self.feature_idx, self.feature_value)

        if X_left.shape[0] == 0 or X_right.shape[0] == 0:
            self.feature_idx = None
            return True
        # mine changes
        if depth > 0:
            self.left_child, self.right_child = Node(), Node()
            self.left_child.train(X_left, y_left, depth - 1)
            self.right_child.train(X_right, y_right, depth - 1)
        # mine changes end
