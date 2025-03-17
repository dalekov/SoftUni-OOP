class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.current = count

    def __iter__(self):
            return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration

        temp = self.current
        self.current -= 1
        return temp

