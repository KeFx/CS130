#   Define a function named sum_of_scores_continue(scores)
#   which takes a list of scores as a parameter. The 
#   function should calculate and return the sum of all 
#   scores in the list that are greater than 0 and less 
#   than 10.

#   If the list contains invalid values, i.e. values which
#   generate a TypeError or a ValueError when converting them 
#   into integers, then the function should ignore those 
#   invalid values and continue computing the sum of the valid
#   scores in the parameter list. For example, if the list
#   contains the following:

#   [-1, 0, 5, 2, 'ten', 35, 45, 9, 20]
#   Then, since 5, 2 and 9 are all valid scores, the 
#   function should return:
#       16

def sum_of_scores_continue(scores):
    total = 0

    for score in scores:
        try:
            score = int(score)
            if 0 < score < 10: 
                total += score
        except (ValueError, TypeError):
            continue
        
    return total
    
print(sum_of_scores_continue(['NA']))