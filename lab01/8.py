def get_smallest_prime_factor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, 20, 2):
        if n % i == 0:
            return i
    return n 

def create_dictionary(numbers):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    
    prime_dict = {prime: [] for prime in primes}
    
    for number in numbers:
        smallest_prime = get_smallest_prime_factor(number)
        
        prime_dict[smallest_prime].append(number)
    
    result_dict = {prime: nums for prime, nums in prime_dict.items() if nums}
    
    return result_dict

numbers_dictionary = create_dictionary([76, 237, 20, 560, 924])
for key in sorted(numbers_dictionary.keys()):
    print(key, numbers_dictionary[key])
values = [76, 237, 20, 560, 924, 351, 561, 133, 102, 147, 415, 126, 121, 780, 17, 1273, 64, 12]
numbers_dictionary = create_dictionary(values)
for key in sorted(numbers_dictionary.keys()):
    print(key, numbers_dictionary[key])
