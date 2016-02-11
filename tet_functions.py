#!/usr/bin/env python
from check import *
import sys

def create_tet(type):
    """Returns tetramino of defined type"""

    if type == 'I':  # Activate 'I' tetramino
        tet = clear_tet(4)
        tet[0] = ['.', '.', '.', '.']
        tet[1] = ['c', 'c', 'c', 'c']
        tet[2] = ['.', '.', '.', '.']
        tet[3] = ['.', '.', '.', '.']
        tet_pos = [0,3]         # Init tet position
        rot = 0
        type = 0
    elif type == 'O':  # Activate 'O' tetramino
        tet = clear_tet(2)
        tet[0] = ['y', 'y']
        tet[1] = ['y', 'y']
        tet_pos = [0,4]
        rot = 0
        type = 1
    elif type == 'Z':  # Activate 'Z' tetramino
        tet = clear_tet(3)
        tet[0] = ["r", "r", "."]
        tet[1] = [".", "r", "r"]
        tet[2] = [".", ".", "."]
        tet_pos = [0,3]
        rot = 0
        type = 2
    elif type == 'S':  # Activate 'S' tetramino
        tet = clear_tet(3)
        tet[0] = [".", "g", "g"]
        tet[1] = ["g", "g", "."]
        tet[2] = [".", ".", "."]
        tet_pos = [0,3]
        rot = 0
        type = 3
    elif type == 'J':  # Activate 'J' tetramino
        tet = clear_tet(3)
        tet[0] = ["b", ".", "."]
        tet[1] = ["b", "b", "b"]
        tet[2] = [".", ".", "."]
        tet_pos = [0,3]
        rot = 0
        type = 4
    elif type == 'L':  # Activate 'L' tetramino
        tet = clear_tet(3)
        tet[0] = [".", ".", "o"]
        tet[1] = ["o", "o", "o"]
        tet[2] = [".", ".", "."]
        tet_pos = [0,3]
        rot = 0
        type = 5
    elif type == 'T':  # Activate 'T' tetramino
        tet = clear_tet(3)
        tet[0] = [".", "m", "."]
        tet[1] = ["m", "m", "m"]
        tet[2] = [".", ".", "."]
        tet_pos = [0,3]
        rot = 0
        type = 6
    ret = [tet,tet_pos]
    return ret

def clear_tet(sqrNum):
    """Clears Active Tet Shape"""
    tet = []  # clear tet
    for i in range(sqrNum):
        tet.append(i)  # create index locations for each tet row
    return tet

def rotate_tet(tet, rot):
    """returns tet matrix rotated 90 deg CW"""
    rotated = zip(*tet[::-1])
    if rot < 3:
        rot += 1
    else:
        rot = 0
    return list(rotated)

def cap_tet(tet):
    """Returns tet in capitalized form"""
    for i in range(0, len(tet)):
        tet[i] = map(str.upper, tet[i])
    return tet

def move_tet(tet_pos, tet, mat, inp, rot, type):
    """Moves active tet in direction specified relative to current pos.
    Returns (tet_pos_new,matrix)"""
    start_y = tet_pos[0]
    start_x = tet_pos[1]
    end_y = tet_pos[0] + len(tet)
    end_x = tet_pos[1] + len(tet[0])
    if inp == '<':
        out=check_space(type, rot)
        tet_pos[1] -= 1  # make new tet_pos one to the left
        if tet_pos[1] >= 0:
            for r in range(0,len(tet)): # For each row of tet
                for i in range((end_x-1),len(mat[r])):
                    mat[start_y+r][i] = '.' # put '.' in each row to the right of tet
        else:
            tet_pos[1] += 1

    elif inp == '>':
        tet_pos[1] += 1  # make new tet_pos one to the right
        if tet_pos[1] <= len(mat[0])-len(tet):
            for r in range(0,len(tet)): # For each row of tet
                for i in range(0,start_x+1):
                    mat[start_y+r][i] = '.' # put '.' in each row to the right of tet
        else:
            tet_pos[1] -= 1

    elif inp == 'v':
        tet_pos[0] += 1  # make new tes_pos one down

    elif inp == 'null':
        pass

    mat = place_tet(mat, tet, tet_pos)  # Use place_tet function to output matrix with tet
    ret = [tet_pos, mat]
    return ret

def place_tet(mat, tet, tet_pos):
    """Returns matrix with activated tet in correct position"""
    start_y = tet_pos[0]
    start_x = tet_pos[1]
    tet = cap_tet(tet)
    for r in range(0, len(tet)):  # For each row of tet
        for i in range(0, len(tet[r])):  # For each item of current row of tet
            mat[start_y + r][start_x + i] = tet[r][i]
    if start_y != 0:  # Check to see if tet is in initial y position
        for i in range(0, len(tet[0])):  # for each item in first row of tet
            mat[start_y - 1][i] = '.'  # put '.' in item spot of previous row
    return mat
