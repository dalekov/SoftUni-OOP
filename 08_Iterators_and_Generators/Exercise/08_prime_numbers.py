def get_primes(this_list):
    for num in this_list:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                yield num



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))