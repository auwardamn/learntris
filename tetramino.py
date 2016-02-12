from tet_functions import *
class tet(object):
    """
    A tetramino has the following properties:

    Properties:
        type - indicates the type of tetramino, as determined by input command
        start_x - indicates the starting left edge of the shape in the matrix (default=None)
        start_y - indicates the starting top edge of the shape in the matrix (default=None)
        end_x - indicates the right edge of the shape in the matrix (depends on start_x and type)
        end_y - indicates the bottom edge of the shape in the matrix (depends on start_y and type)
        space_r- number of blank columns in shape matrix on right
        space_l- number of blank columns in shape matrix on left
        space_t- number of blank rows in shape matrix on top
        space_b- number of blank rows in shape matrix on bottom
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
        self.end_x, self.end_y = end_cond(shape, start_x, start_y)
        self.space_r = None
        self.space_l = None
        self.space_t = None
        self.space_b = None

    def rotate(self):
        """returns tet matrix rotated 90 deg CW"""
        self.shape = zip(*self.shape[::-1])
        if self.rot < 3:
                self.rot += 1
        else:
                self.rot = 0
        check_space(self)
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
        check_space(self)
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
        check_space(self)
        if inp == '<':
            self.start_x -= 1  # make new tet_pos one to the left
            if self.start_x >= 0:
                for r in range(0,len(self.shape)): # For each row of tet
                    for i in range((self.end_x-1),len(mat[r])):
                        mat[self.start_y+r][i] = '.' # put '.' in each row to the right of tet
            else:
               self.start_x += 1

            #If there is space on left
            if self.space_l != 0:
                self.start_x -= 1

        elif inp == '>':
            self.start_x += 1  # make new tet_pos one to the right
            if self.end_x < len(mat[0]):
                for r in range(0,len(self.shape)): # For each row of tet
                    for i in range(0,self.start_x+1):
                        mat[self.start_y+r][i] = '.' # put '.' in each row to the right of tet
            else:
               self.start_x -= 1

            #If there is space on right
            if self.space_r != 0:
                self.start_x += 1

        elif inp == 'v':
            self.start_y += 1  # make new tes_pos one down

        elif inp == 'null':
            pass

        self.end_x, self.end_y = end_cond(self.shape, self.start_x, self.start_y)
        mat = self.place(mat)  # Use place_tet function to output matrix with tet
        return mat