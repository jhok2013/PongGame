class Point(object):
    '''
    Represents the x and y coordinates of the ball or paddle
    '''
    x: int
    y: int

    def __init__(self, x: int, y: int):
        '''
        Initializes the object with set coordinates
        '''
        self.x = x
        self.y = y