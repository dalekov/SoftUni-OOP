def even_parameters(func):
    def wrapper(*args):
        if any(not isinstance(x, int) or x % 2 == 1 for x in args):
            return "Please use only even numbers!"
        res = func(*args)
        return res
    return wrapper


