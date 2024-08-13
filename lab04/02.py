def get_cube_volume(length):

    try:
        length = float(length)

    except TypeError:
        return (0, 'ERROR: The type is incorrect!')
    
    except ValueError:
        return (0, 'ERROR: The value is invalid!')
    
    else:
        if length == 0:
            return (0, 'ERROR: Not a cube!')
        elif length < 0:
            return (0, 'ERROR: Length must be positive!')
        return (round(length**3), '')

print(round(get_cube_volume(10.5), 0) 
