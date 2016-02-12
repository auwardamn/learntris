def get_width(shape):
    """Returns width of given tet shape"""
    return len(shape)

def end_cond(shape, start_x, start_y):
    """Returns (end_x,end_y) based on given tet shape and tet pos"""
    width = get_width(shape)
    end_x = start_x + width
    end_y = start_y + width
    return end_x, end_y

def clear_tet(sqrNum):
    """Clears Active Tet Shape"""
    tet = []  # clear tet
    for i in range(sqrNum):
        tet.append(i)  # create index locations for each tet row
    return tet

def create_shape(type):
    if type == 'I':  # Activate 'I' tetramino
        tet = clear_tet(4)
        tet[0] = ['.', '.', '.', '.']
        tet[1] = ['c', 'c', 'c', 'c']
        tet[2] = ['.', '.', '.', '.']
        tet[3] = ['.', '.', '.', '.']
        start_x = 3         # Init tet position
    elif type == 'O':  # Activate 'O' tetramino
        tet = clear_tet(2)
        tet[0] = ['y', 'y']
        tet[1] = ['y', 'y']
        start_x = 4
    elif type == 'Z':  # Activate 'Z' tetramino
        tet = clear_tet(3)
        tet[0] = ["r", "r", "."]
        tet[1] = [".", "r", "r"]
        tet[2] = [".", ".", "."]
        start_x = 3
    elif type == 'S':  # Activate 'S' tetramino
        tet = clear_tet(3)
        tet[0] = [".", "g", "g"]
        tet[1] = ["g", "g", "."]
        tet[2] = [".", ".", "."]
        start_x = 3
    elif type == 'J':  # Activate 'J' tetramino
        tet = clear_tet(3)
        tet[0] = ["b", ".", "."]
        tet[1] = ["b", "b", "b"]
        tet[2] = [".", ".", "."]
        start_x = 3
    elif type == 'L':  # Activate 'L' tetramino
        tet = clear_tet(3)
        tet[0] = [".", ".", "o"]
        tet[1] = ["o", "o", "o"]
        tet[2] = [".", ".", "."]
        start_x = 3
    elif type == 'T':  # Activate 'T' tetramino
        tet = clear_tet(3)
        tet[0] = [".", "m", "."]
        tet[1] = ["m", "m", "m"]
        tet[2] = [".", ".", "."]
        start_x = 3
    return tet, start_x

def check_space(tet):
    """returns number of spaces on all sides of active tet
    output dictionary: (space_r,space_b,space_l,space_t)"""
    if tet.type == 'I':       #type I
        if tet.rot == 0:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 2
        elif tet.rot == 1:
            space_r = 1
            space_l = 2
            space_t = 0
            space_b = 0
        elif tet.rot == 2:
            space_r = 0
            space_l = 0
            space_t = 2
            space_b = 1
        elif tet.rot == 3:
            space_r = 2
            space_l = 1
            space_t = 0
            space_b = 0
    elif tet.type == 'O':     #type O
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 0
    elif tet.type == 'Z':     #type Z
        if tet.rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif tet.rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif tet.rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif tet.rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    elif tet.type == 'S':     #type S
        if tet.rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif tet.rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif tet.rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif tet.rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    elif tet.type == 'J':     #type J
        if tet.rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif tet.rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif tet.rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif tet.rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    elif tet.type == 'L':     #type L
        if tet.rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif tet.rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif tet.rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif tet.rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    elif tet.type == 'T':     #type T
        if tet.rot == 0:
            space_r = 0
            space_l = 0
            space_t = 0
            space_b = 1
        elif tet.rot == 1:
            space_r = 0
            space_l = 1
            space_t = 0
            space_b = 0
        elif tet.rot == 2:
            space_r = 0
            space_l = 0
            space_t = 1
            space_b = 0
        elif tet.rot == 3:
            space_r = 1
            space_l = 0
            space_t = 0
            space_b = 0
    tet.space_r= space_r
    tet.space_b= space_b
    tet.space_l= space_l
    tet.space_t= space_t
    return tet.space_r, tet.space_b, tet.space_l, tet.space_t