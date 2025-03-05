class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def subtract(*args):
        total = args[0]
        for arg in args[1:]:
            total -= arg

        return total

    @staticmethod
    def multiply(*args):
        total = 1
        for arg in args:
            total *= arg

        return total

    @staticmethod
    def divide(*args):
        total = args[0]
        for arg in args[1:]:
            total /= arg

        return total