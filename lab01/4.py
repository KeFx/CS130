def get_largest_prime_factor(number):
    
    primes_under_23 = [2, 3, 5, 7, 11, 13, 17, 19]

    prime_factors = []
    
    for prime in primes_under_23:
        if number % prime == 0:
            prime_factors.append(prime)

    return max(prime_factors)

print(get_largest_prime_factor(46))
