def get_building_name(building_dictionary, building_number):
    try:
        building_number = int(building_number)
        return building_dictionary[building_number]
        
    except KeyError:
        print(f"ERROR: {building_number} is not available.")
        
    except (TypeError, ValueError):
        print("ERROR: Invalid number!")

    
