class Vector:
    def __init__(self, values):
        self.values = list(values)

    def __add__(self, other):
        result_values = [x + y for x, y in zip(self.values, other.values)]
        return Vector(result_values)

    def __sub__(self, other):
        result_values = [x - y for x, y in zip(self.values, other.values)]
        return Vector(result_values)

    def __mul__(self, other):
        result_values = [x * y for x, y in zip(self.values, other.values)]
        return Vector(result_values)

    def __matmul__(self, other):
        result = sum(x * y for x, y in zip(self.values, other.values))
        return result

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value

    def __eq__(self, other):
        return self.values == other.values
