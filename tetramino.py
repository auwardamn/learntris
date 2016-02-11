import sys

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

class tet(object):
    """
    A tetramino has the following properties:

    Properties:
        type - indicates the type of tetramino, as determined by input command
        start_x - indicates the starting left edge of the shape in the matrix (default=None)
        start_y - indicates the starting top edge of the shape in the matrix (default=None)
        end_x - indicates the right edge of the shape in the matrix (depends on start_x and type)
        end_y - indicates the bottom edge of the shape in the matrix (depends on start_y and type)
        space[] - list containing number of blank rows in shape matrix vs actual shape (r,b,l,t)
        rot - index of rotation: def=0, 1=90, 2=180, 3=270
        shape[] - list the forms the current visual representation of the tet (matrix form)
    """
    def __init__(self, type, start_x=None, start_y=0, rot=0):
        if start_x:
            shape = create_shape(type)[0]
        else:
            shape, start_x = create_shape(type)
        self.type = type
        self.shape = shape
        self.start_x = start_x
        self.start_y = start_y
        self.rot = rot
        self. end_x, self.end_y = end_cond(shape, start_x, start_y)

    def rotate(self):
        """returns tet matrix rotated 90 deg CW"""
        self.shape = zip(*self.shape[::-1])
        if self.rot < 3:
                self.rot += 1
        else:
                self.rot = 0
        return list(self.shape), self.rot

    def cap_tet(self):
        """Returns shape in capitalized form"""
        for i in range(0, len(self.shape)):
            self.shape[i] = map(str.upper, self.shape[i])
        return self.shape

    def low_tet(self):
        """Returns shape in lowercase form"""
        for i in range(0, len(self.shape)):
            self.shape[i] = map(str.lower, self.shape[i])
        return self.shape

    def place(self, mat):
        """Returns matrix with activated tet in correct position"""
        tet = self.cap_tet()
        for r in range(0, len(tet)):  # For each row of tet
            for i in range(0, len(tet[r])):  # For each item of current row of tet
                mat[self.start_y + r][self.start_x + i] = tet[r][i]
        if self.start_y != 0:  # Check to see if tet is in initial y position
            for i in range(0, len(tet[0])):  # for each item in first row of tet
                mat[self.start_y - 1][i] = '.'  # put '.' in item spot of previous row
        return mat

    def move(self, inp, mat):
        """Moves active tet in direction specified relative to current pos.
        Returns matrix, and updates self properties"""
        if inp == '<':
            self.start_x -= 1  # make new tet_pos one to the left
            if self.start_x >= 0:
                for r in range(0,len(self.shape)): # For each row of tet
                    for i in range((self.end_x-1),len(mat[r])):
                        mat[self.start_y+r][i] = '.' # put '.' in each row to the right of tet
            else:
                self.start_x += 1

        elif inp == '>':
            self.start_x += 1  # make new tet_pos one to the right
            if self.end_x < len(mat[0]):
                for r in range(0,len(self.shape)): # For each row of tet
                    for i in range(0,self.start_x+1):
                        mat[self.start_y+r][i] = '.' # put '.' in each row to the right of tet
            else:
                self.start_x -= 1

        elif inp == 'v':
            self.start_y += 1  # make new tes_pos one down

        elif inp == 'null':
            pass

        self.end_x, self.end_y = end_cond(self.shape, self.start_x, self.start_y)
        mat = self.place(mat)  # Use place_tet function to output matrix with tet
        return mat