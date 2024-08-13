def is_child(age):
    
    try:
        age = int(age)
        
    except TypeError:
        return (False, "ERROR: The type is incorrect!")

    except ValueError:
        return (False, "ERROR: The value is invalid!")

    else:
        return (0 <= age <= 12, age)

data = is_child(8)
print(data)
print(type(data))
print(type(data[0]), type(data[1]))
print(4.5, is_child(4.5))
print(-12, is_child(-12))
print(0, is_child(0))
print('12', is_child('12'))
print('Ten', is_child('Ten'))
print([12], is_child([12]))
