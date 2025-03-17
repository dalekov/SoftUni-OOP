def solution():

    def integers():
        current_value = 0
        while True:
            current_value += 1
            yield current_value

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        count = 0
        result = []
        for item in seq:
            if count >= n:
                break
            result.append(item)
            count += 1
        return result

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
