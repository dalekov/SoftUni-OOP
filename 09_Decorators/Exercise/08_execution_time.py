import time

def exec_time(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        return end - start
    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))

