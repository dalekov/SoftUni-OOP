def read_next(*args):

    for arg in args:
        for item in arg:
            yield item


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
