import itertools

def possible_permutations(my_list):
    p = itertools.permutations(my_list)

    for perm in p:
        yield list(perm)