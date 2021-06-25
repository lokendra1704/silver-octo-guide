class Squares:
    def __init__(self, MAX_SQUARE):
        self.maxsquare = MAX_SQUARE
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter>self.maxsquare:
            raise StopIteration("Completed")
        value = self.counter
        self.counter+=1
        return value**2

for i in Squares(5):
    print(i)