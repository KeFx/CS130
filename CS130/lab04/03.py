def sum_of_multiples_of_5(numbers, start_index, end_index):

    total = 0
    
    try:
        for index in range(start_index, end_index+1):
            print(numbers[index])
            if numbers[index] % 5 == 0:
                total += numbers[index]

    except IndexError:
        print("ERROR: Out of range!")
        return 0

    except (ValueError, TypeError):
        print("ERROR: Invalid number!")
        return 0

    else:
        return total

	
list1 = [5, 2, 15]
print(sum_of_multiples_of_5(list1, 2, 6))
