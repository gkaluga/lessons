numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    if numbers[i] < 2:
        continue
    is_prime = True

    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print('primes:', primes)
print('not_primes:', not_primes)
