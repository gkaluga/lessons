def is_prime(fu):
    def wrapper(a1, a2, a3):
        result = fu(a1, a2, a3)
        typ_ = 'Простое'
        for i in range(2, result):
            if result % i == 0:
                typ_ = 'Составное'
                break
        print(typ_)
        return result

    return wrapper


@is_prime
def sum_three(a1, a2, a3):
    return a1 + a2 + a3


result = sum_three(2, 3, 6)
print(result)
