class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.items_returned = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.items_returned >= self.number:
            raise StopIteration

        item = self.sequence[self.index]

        self.index = (self.index + 1) % len(self.sequence)

        self.items_returned += 1
        return item



result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

