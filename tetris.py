#!/usr/bin/env python
from __future__ import print_function
import sys
from tet_functions import *
from mat_functions import *

# Define Functions
def grab_command():
    """Gets command input from user, splits command strings into command list"""
    input = sys.stdin.readline()  # Get Command Input
    command_list = []
    for i in input:
        command_list.append(i)
    return command_list

# Init Variables
width = 10
height = 22
score = 0
cleared = 0
ex = 0
matrix = create_empty_matrix(width, height)
tet_pos = [0, 0]  # tet_pos[0] = y, tet_pos[1]=x
tet = []
rot = 0
type = 0

while ex == 0:  # Main Loop

    # Read Commands
    command_list = grab_command()
    for x in range(0, len(command_list)):  # "For Each Command Entered"
        command = command_list[x]  # Set Current Command
        # Execute Possible Commands
        if command.strip() == 'p':  # Print Current Matrix Status
            print_matrix(matrix)

        elif command.strip() == 'g':  # Input New Matrix Status
            for i in range(0, height):  # For each row, as defined by the height
                input = sys.stdin.readline()  # Get input lines
                item_list = str.split(input)  # Split Lines into Items
                matrix[i] = item_list  # Put list of items into current row

        elif command.strip() == 'c':  # Clear Matrix
            matrix = create_empty_matrix(width, height)

        elif command.strip() == '?':  # Request Counter
            x = x + 1  # Skip to next command in command_list
            command = command_list[x]
            if command.strip() == 's':  # If score request, print score
                print(score)

            elif command.strip() == 'n':  # If line clear request, print line clear number
                print(cleared)

        elif command.strip() == 's':  # Check For Solid Lines
            for i in range(0, height):
                line = str(matrix[i])
                if line.find('.') == -1:  # Clear if needed and add to scores
                    matrix = clear_row(matrix, i)
                    cleared = cleared + 1
                    score = score + 100

        elif (command.strip() == 'I' or
                      command.strip() == 'O' or
                      command.strip() == 'Z' or
                      command.strip() == 'S' or
                      command.strip() == 'J' or
                      command.strip() == 'L' or
                      command.strip() == 'T'):
            out = create_tet(command.strip())
            tet = out[0]
            tet_pos = out[1]

        elif command.strip() == 't':  # Display Active Tetramino
            print_matrix(tet)

        elif command.strip() == ')':  # Rotate Tetramino
            tet = (rotate_tet(tet, rot))

        elif command.strip() == ';':  # Print Gap Line
            print(' ')

        elif command.strip() == '<':
            out =  move_tet(tet_pos, tet, matrix, '<', rot, type)
            tet_pos = out[0]
            #print(tet_pos)
            matrix = out[1]

        elif command.strip() == 'v':
            out = move_tet(tet_pos, tet, matrix, 'v', rot, type)
            tet_pos = out[0]
            matrix = out[1]

        elif command.strip() == '>':
            out = move_tet(tet_pos, tet, matrix, '>', rot, type)
            tet_pos = out[0]
            #print(tet_pos)
            matrix = out[1]

        elif command.strip() == 'P':  # Print Active Tetramino in Matrix
            if tet == []:
                print("Tet not yet defined")
            else:
                out = move_tet(tet_pos, tet, matrix, 'null', rot, type)
                tet_pos = out[0]
                matrix = out[1]
                print_matrix(matrix)

        elif command.strip() == 'q':  # Quit Command
            ex = 1  # Terminate Program

        elif command == '\n' or 'n':
            continue

        else:  # Invalid Input
            print('Command Not Recognized')
