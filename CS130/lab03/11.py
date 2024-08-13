def append_double_to(element, values=None):
    print('values =', values)
    print('element =', element)
    if values == None:
        return [element*2]

    values.append(element*2)

my_list = []
append_double_to(12, my_list )
print(my_list)

##my_list = append_double_to(12)
##
##print()
##
##print("my_list =", my_list)
##my_list = append_double_to(12, my_list)
##
##print()
##
##print("my_list =", my_list)
##my_list = append_double_to(24)
##
##print("my_list =", my_list)
