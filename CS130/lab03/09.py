def remove_zeros(numbers):
    numbers = [x for x in numbers if x != 0]


numbers = [0, 15, -2, 35, 135, 7]
##numbers = [number for number in numbers if number != 0]
##print(numbers)
remove_zeros(numbers)
print(numbers)
##
##
##lst = ['A', 'B', 'C']
##lst = [x for x in lst if x != 'A']
##print(lst)
