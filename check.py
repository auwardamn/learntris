#!/usr/bin/env python
space_r = 0
space_l = 0
space_t = 0
space_b = 0
def check_space(type, rot):
    """returns number of spaces on all sides of active tet
    output list (space_r,space_l,space_t,space_b)"""
    if type == 0:       #type I
        if rot == 0:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 2
        elif rot == 1:
            space_r = 1
            space_l = 2
            space_t = 0
            space_b = 0
        elif rot == 2:
            space_r = 0
            space_l = 0
            space_t = 2
            space_b = 1
        elif rot == 3:
            space_r = 2
            space_l = 1
            space_t = 0
            space_b = 0
    elif type == 1:     #type O
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 0
    elif type == 2:     #type Z
        if rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    elif type == 3:     #type S
        if rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    elif type == 4:     #type J
        if rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    elif type == 5:     #type L
        if rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    elif type == 6:     #type T
        if rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    ret = [space_r,space_l,space_t,space_b]
    return ret