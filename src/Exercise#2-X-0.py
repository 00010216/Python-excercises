"""
Run in python version 3.8.10, numpy 1.20.3
"""
import numpy as np 

"""
Turns subarray (row, column or diagonal) into a string 
and counts if there are 3 x or 0 in the string 
"""
def verify(subarray):
    subarray_toString = np.array_str(subarray)
    if(subarray_toString.upper().count("X") == 3):
        return("X")
    if(subarray_toString.count("0") == 3):
        return("0")
    else: return "None"

"""
Creates a list with the subarrays of (rows,columns and diagonals)
then it iterates the list and verifys for each item list if it is the winner
"""
def detect_winner(game):
    #corra lista y envia variables
    subarrays_list = [game[0],game[1],game[2], game[:,0],game[:,1],game[:,2], np.diag(game), np.fliplr(game).diagonal()]
    for x in subarrays_list:
        winner = verify(x)
        #print(winner)
        if (winner != "None"):
            return winner
    return "There is no winner"

#Main code    
game = np.array([["0","0","x"],[None,"0","X"],["X","0","x"]])
winner = detect_winner(game)
print(winner)