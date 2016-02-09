#!/usr/bin/env python
from __future__ import print_function
import sys

def create_empty_matrix(m,n):
    """Returns an mxn empty (.) matrix"""
    matrix=[]
    for i in range (0,n):
        row=[]
        for i in range (0,m):
            row.append('.')
        matrix.append(row)
    return matrix

def clear_tet(sqrNum):
    """Clears Active Tet Shape"""
    tet=[]  #clear tet
    for i in range(sqrNum):
            tet.append(i)   #create index locations for each tet row
    return tet

def clear_row(matrix, row_num):
    """Returns Matrix with requested row cleared"""
    width=len(matrix[1])
    matrix[row_num]=[]
    for i in range(0,width): # Do as many times as items per row
        matrix[row_num].append('.')
    return matrix

def create_tet(type):
    """Returns tetramino of defined type"""
    
    if type == 'I':    #Activate 'I' tetramino
        tet = clear_tet(4)
        tet[0]=['.','.','.','.']
        tet[1]=['c','c','c','c']
        tet[2]=['.','.','.','.']
        tet[3]=['.','.','.','.']
    
    elif type == 'O':    #Activate 'O' tetramino
        tet = clear_tet(2)
        tet[0]=['y','y']
        tet[1]=['y','y']

    elif type == 'Z':    #Activate 'Z' tetramino
            tet = clear_tet(3)
            tet[0]=["r","r","."]
            tet[1]=[".","r","r"]
            tet[2]=[".",".","."]
    
    elif type == 'S':    #Activate 'S' tetramino
            tet = clear_tet(3)
            tet[0]=[".","g","g"]                
            tet[1]=["g","g","."]
            tet[2]=[".",".","."]

    elif type == 'J':    #Activate 'J' tetramino
            tet = clear_tet(3)
            tet[0]=["b",".","."]
            tet[1]=["b","b","b"]
            tet[2]=[".",".","."]

    elif type == 'L':    #Activate 'L' tetramino
            tet = clear_tet(3)
            tet[0]=[".",".","o"]
            tet[1]=["o","o","o"]
            tet[2]=[".",".","."]

    elif type == 'T':    #Activate 'T' tetramino
            tet = clear_tet(3)
            tet[0]=[".","m","."]
            tet[1]=["m","m","m"]
            tet[2]=[".",".","."]
    return tet

def print_matrix(matrix):
    """prints provided matrix of seperate elements to the screen with " " seperation"""
    for i in range(0,len(matrix)): #For Each row of the matrix
        print(*matrix[i], sep=" ") #Print Each item of current row with " " seperation

def rotate_tet(tet):
    """returns tet matrix rotated 90 deg CW"""
    rotated = zip(*tet[::-1])
    return list(rotated)

def cap_tet(tet):
    """Returns tet in capitalized form"""
    for i in range(0,len(tet)):
        tet[i]=map(str.upper,tet[i])
    return tet

def place_tet(mat, t):
    """Places activated tet in matrix"""
    t=cap_tet(t)
    for r in range(0,len(tet)): #For each row of tet
        if len(t) == 2:
            start = 4
        else:
            start = 3
        for i in range(0,len(tet[r])): #For each item in row of tet
            mat[r][start] = tet[r][i]
            start = start + 1
    return mat

def grab_command():
    """Gets command input from user, splits command strings into command list"""
    input = sys.stdin.readline()                # Get Command Input
    command_list= []
    for i in input:
            command_list.append(i)
    return command_list

# Init Variables
width = 10
height = 22
score=0
cleared=0
ex=0
matrix=create_empty_matrix(width,height)

while ex==0:                #Main Loop

    #Read Commands
    command_list = grab_command()
    for x in range(0,len(command_list)):        # "For Each Command Entered"
        command = command_list[x]    # Set Current Command
        # Execute Possible Commands
        if command.strip() == 'p':      # Print Current Matrix Status
            print_matrix(matrix)

        elif command.strip() == 'g':    # Input New Matrix Status
            for i in range(0,height):   # For each row, as defined by the height
               input=sys.stdin.readline() # Get input lines
               item_list = str.split(input) # Split Lines into Items
               matrix[i] = item_list # Put list of items into current row

        elif command.strip() == 'c':    # Clear Matrix
            matrix=create_empty_matrix(width,height)

        elif command.strip() == '?':    #Request Counter
            x = x+1                     #Skip to next command in command_list
            command = command_list[x]
            if command.strip() == 's':  #If score request, print score
                print(score)

            elif command.strip() == 'n':#If line clear request, print line clear number
                print(cleared)

        elif command.strip() == 's':    # Check For Solid Lines
            for i in range(0,height):
                line = str(matrix[i])
                if line.find('.') == -1:    #Clear if needed and add to scores
                    matrix=clear_row(matrix, i)
                    cleared=cleared+1
                    score=score+100
        
        elif (command.strip() == 'I' or
                command.strip() == 'O' or
                command.strip() == 'Z' or
                command.strip() == 'S' or
                command.strip() == 'J' or
                command.strip() == 'L' or
                command.strip() == 'T'):
            tet=create_tet(command.strip())

        elif command.strip() == 't':    #Display Active Tetramino
            print_matrix(tet)

        elif command.strip() == ')':    #Rotate Tetramino
            tet=(rotate_tet(tet))

        elif command.strip() == ';':    #Print Gap Line
            print(' ')

        elif command.strip() == 'P':    #Print Active Tetramino in Matrix
            matrix = place_tet(matrix,tet)
            print_matrix(matrix)

        elif command.strip() == 'q':    # Quit Command
            ex=1                        # Terminate Program

        elif command == '\n' or 'n':
            continue

        else:                          # Invalid Input
            print('Command Not Recognized')