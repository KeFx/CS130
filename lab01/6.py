def remove_multiples_of_3_but_not_2(numbers):
    numbers[:] = [n for n in numbers if not (n % 3 == 0 and n % 2 != 0)]


values = [36, 19, 29, 42, 15, 15, 6, 15, 48, 48, 23, 31, 18, 2, 35, 24, 7]
remove_multiples_of_3_but_not_2(values)
print(values)
