class Velocity(object):
    '''
    Represents the velocity of the ball
    '''
    dx: float
    xy: float

    def __init__(self, dx: float, dy: float):
        '''
        Initializes the velocity with the provided
        x and y velocity
        '''
        self.dx = dx
        self.dy = dy