class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count

        self.current_step = 0
        self.i = -self.step


    def __iter__(self):
        return self

    def __next__(self):
        if self.current_step >= self.count:
            raise StopIteration

        self.current_step += 1
        self.i += self.step
        return self.i





numbers = take_skip(10, 5)
for number in numbers:
    print(number)