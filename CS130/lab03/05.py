def get_median_value(input_):
    numbers = [number for number in input_]
    numbers.sort()
    if len(numbers) % 2 != 0: #odd number of elements
        return numbers[len(numbers)//2]
    mid_index = len(numbers)//2
    return (numbers[mid_index-1] + numbers[mid_index]) / 2

numbers = [3, 9, 4]
print(get_median_value(numbers))
print(numbers)
print(get_median_value([13, 10, 9, 3]))
print(get_median_value([13, 10, 9, 3, 4]))
