class custom_range:
    def __init__(self, start, end):
        self.i = start
        self.n = end

        self.temp = self.i - 1

    def __iter__(self): # Върху какво итерираме
        return self

    def __next__(self): # Как итерираме
        self.temp += 1
        if self.temp > self.n:
            raise StopIteration
        return self.temp


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
