class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.items = iter(self.dictionary.items())



    def __iter__(self):
        return self

    def __next__(self):
        return next(self.items)





result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
