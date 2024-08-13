def square_odds(numbers_list):
    for i, n in enumerate(numbers_list):
        if n % 2 != 0:
            numbers_list[i] = n**2

numbers_list = [1, 5, 12, 6, 7]
print(numbers_list)
square_odds(numbers_list)
print(numbers_list)
