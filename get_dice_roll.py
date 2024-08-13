    # To simulate a dice roll, define a function named 
    # get_dice_roll() that repeatedly prompts the user for 
    # input until they enter a valid integer between 1 and 6, 
    # inclusive. 

    # The function should handle invalid inputs, such as 
    # values outside this range or inputs that cause a 
    # TypeError or ValueError, by continuing to prompt the 
    # user until a valid value is entered. Once a valid 
    # integer is entered, the function should return that 
    # integer.

def get_dice_roll():
    roll = None
    while roll < 1 or roll > 6:
        