# Objective: Create a TicTacToe game where 2 players try to make a line of X or O on horizontal,vertical or diagonal
# The grid is composed of a 3x3. If a player can make a line he will obtain the victory, else if noone can make a line it will result in a draw

# Step1: Game starts with X, players deciding who will start first.
# Step2: Each player will need to insert the number of the grid which can be seen constantly during the game in the form

# ["1"] ["2"] ["3"]
# ["4"] ["5"] ["6"]
# ["7"] ["8"] ["9"]
# Like this when the player tries to insert a number it will be compared with the number in the spot and the O or X will be inserted
# Else if the space is already occupied by X or O a message will appear and the user will have to insert a valid free spot.

# Step3: starting with round5 (the 5th move out of 9 moves) the game will check after each input if there is a match on the grid.

# Part2: Create a second gamemode where the player can play vs the computer
# Step1: The first turn will be decided by the random function (50/50 chance)
# Step2: the computer will choose at random from an array of available spots where to place its X or O
# Step3: this array will be updated after every turn optimizing the time and effort required by the computer to make its next move
#Example: random([1,2]) = 50% , random([1,2,3]) = 33%, random([1,2,3,4]) = 25%, random([1,2,3,4,5]) = 20% and so on 

# POSSIBLE UPGRADE
#initiate from the very beggining possible_tiles list so whenever the player or computer makes a move
# the only action is to remove the number from the list. This way we can delete the for loop which generates the list

import random as RNG

print("WELCOME TO TicTacToe")
print("Want to play alone or with a friend?")
check_x = True
while check_x == True:
        x= input("Input [1] for friend ,[2] for alone: ")
        if(x == str(1)):
            check_x = False
        elif (x == str(2)):
            check_x = False
        else: 
            print("Invalid option. Try again.")
            check_x = True

#the definition which handles X or O inseration of the player
def InsertIntoSpot(check_x, type, Matrix): 
    while(check_x == True):
        x= input("Input spot number for "+ type+ " ")
        if(int(x) >=1 and int(x)<=9):
            for spot in range(0,len(Matrix)):
                #print("spot is" ,spot)
                if(str(int(x)-1) == str(spot)):
                    if (str(int(x)-1) == str(spot) and (str(Matrix[spot]) == "x" or str(Matrix[spot])== "o")):
                        print("Spot already taken. Try again")
                        check_x= True
                    else:
                        Matrix[spot] = type
                        #print(Matrix)
                        check_x = False
                        break 
        else: 
            print("Invalid option. Try again.")
            check_x = True
    return Matrix

#the definition which handles X or O inseration of the computer
def ComputerInsertIntoSpot(check_x, type, Matrix):
    # its possible to initiate from the very beggining possible_tiles list so whenever the player or computer makes a move
    # the only action is to remove the number from the list. This way we can delete the for loop which generates the list
    possible_tiles = []
    for spot in range(0,len(Matrix)):
        if(Matrix[spot] != "o" and Matrix[spot] != "x"):
            possible_tiles.append(spot)
    #x obtains a random value from the list above and makes its move
    x= RNG.choice(possible_tiles)
    for spot in range(0,len(Matrix)):
        #print("spot is" ,spot)
        if(str(x) == str(spot)):
            Matrix[spot] = type    
            #print(Matrix)
            break 
    return Matrix

# shows the elements of the matrix 3 at a time per row
def ShowCurrentMatrix(matrix):
    for spot in range(0,len(matrix),3):
        print(matrix[spot]," ",matrix[spot+1]," ",matrix[spot+2],"\n")

#checks every line column and diagonal for possible matches after round5 for X and round 6 for O
def Check_solution(matrix):
    if (matrix[0] == matrix[1] == matrix[2] == "x"): #line 1
        return "x"
    if (matrix[0] == matrix[1] == matrix[2] == "o"):
        return "o"
    if (matrix[3] == matrix[4] == matrix[5] == "x"): #line 2
        return "x"
    if (matrix[3] == matrix[4] == matrix[5] == "o"): 
        return "o"
    if (matrix[6] == matrix[7] == matrix[8] == "x"): #line 3
        return "x"   
    if (matrix[6] == matrix[7] == matrix[8] == "o"):
        return "o"   
    if(matrix[0] == matrix[3] == matrix[6] == "x"): #col 1
        return "x"
    if(matrix[0] == matrix[3] == matrix[6] == "o"): 
        return "o"
    if(matrix[1] == matrix[4] == matrix[7] == "x"): #col 2
        return "x"
    if(matrix[1] == matrix[4] == matrix[7] == "o"):
        return "o"
    if(matrix[2] == matrix[5] == matrix[8] == "x"): #col 3
        return "x"
    if(matrix[2] == matrix[5] == matrix[8] == "o"): 
        return "o"
    if(matrix[0] == matrix[4] == matrix[8] == "x"): #primary diagonal
        return "x"
    if(matrix[0] == matrix[4] == matrix[8] == "o"): 
        return "o"
    if(matrix[2] == matrix[4] == matrix[6] == "x"): #secondary diagonal
        return "x"
    if(matrix[2] == matrix[4] == matrix[6] == "o"): 
        return "o"
                 
Matrix = ["1","2","3",
          "4","5","6",
          "7","8","9"]

#Start of Player vs Player if
if(int(x)==1):
    print("Decide which player will start first with X")
    ShowCurrentMatrix(Matrix)
    unavailable_spots = 0
    start_check_solution = 0
    match_found_x = False
    match_found_o = False
    while ((match_found_x == False) or (match_found_o == False)) and not unavailable_spots ==9:
        if(unavailable_spots %2 ==0):
            InsertIntoSpot(True,"x",Matrix)
            ShowCurrentMatrix(Matrix)
            unavailable_spots = unavailable_spots+1
            start_check_solution = start_check_solution +1
            if(start_check_solution >=5):
                if(Check_solution(Matrix) == "x"):
                    match_found_x = True
                    break    
            
        else:
            InsertIntoSpot(True,"o",Matrix)
            ShowCurrentMatrix(Matrix)
            unavailable_spots = unavailable_spots+1
            start_check_solution = start_check_solution +1
            if(start_check_solution >=6):
                if(Check_solution(Matrix) == "o"):
                    match_found_o = True    
                    break

#Start of Player vs Computer if
if(int(x)==2):
    #rng to check if computer or player makes the 1st move
    # 0 for player, 1 for computer
    goes_first = RNG.randrange(0,1)
    #depending on who goes first the statements will wary by which Computer/InsertIntoSpot will be played in IF and Else
    
    if(goes_first == 0): #player play
        print("Player goes first with X")
        ShowCurrentMatrix(Matrix)
        unavailable_spots = 0
        start_check_solution = 0
        match_found_x = False
        match_found_o = False
        while ((match_found_x == False) or (match_found_o == False)) and not unavailable_spots ==9:
            if(unavailable_spots %2 ==0):
                InsertIntoSpot(True,"x",Matrix)
                ShowCurrentMatrix(Matrix)
                unavailable_spots = unavailable_spots+1
                start_check_solution = start_check_solution +1
                if(start_check_solution >=5):
                    if(Check_solution(Matrix) == "x"):
                        match_found_x = True
                        break    
                
            else: #computer play
                print("computer plays o")
                ComputerInsertIntoSpot(True,"o",Matrix)
                ShowCurrentMatrix(Matrix)
                unavailable_spots = unavailable_spots+1
                start_check_solution = start_check_solution +1
                if(start_check_solution >=6):
                    if(Check_solution(Matrix) == "o"):
                        match_found_o = True    
                        break
                    
    else:
        print("Computer goes first with X")
        unavailable_spots = 0
        start_check_solution = 0
        match_found_x = False
        match_found_o = False
        while ((match_found_x == False) or (match_found_o == False)) and not unavailable_spots ==9:
            if(unavailable_spots %2 ==0): #computer play
                print("computer plays x")
                ComputerInsertIntoSpot(True,"x",Matrix)
                ShowCurrentMatrix(Matrix)
                unavailable_spots = unavailable_spots+1
                start_check_solution = start_check_solution +1
                if(start_check_solution >=5):
                    if(Check_solution(Matrix) == "x"):
                        match_found_x = True
                        break    
                
            else: #player play
                InsertIntoSpot(True,"o",Matrix)
                ShowCurrentMatrix(Matrix)
                unavailable_spots = unavailable_spots+1
                start_check_solution = start_check_solution +1
                if(start_check_solution >=6):
                    if(Check_solution(Matrix) == "o"):
                        match_found_o = True    
                        break
    
#check at the end the result status if its a tie or a win for X or O            
if(unavailable_spots == 9 and match_found_x == False and match_found_o == False):
    print("Its a tie")
if(match_found_x == True):
    print("Winner is x")
if(match_found_o == True):
    print("Winner is o")