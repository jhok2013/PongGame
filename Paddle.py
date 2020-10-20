from Point import Point

import arcade

class Paddle(object):
    '''
    The paddle object for the pong game.
    '''

    center: Point

    def __init__(self):
        '''

        '''
        center: Point = Point(
            x=20,
            y=150
        )
        self.center = center
    
    def draw(self):
        '''
        Draws the paddle in the middle of the board.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        height: int = 50
        width: int = 10
        arcade.draw_rectangle_outline(
            center_x=self.center.x,
            center_y=self.center.y,
            width=width,
            height=height,
            color=arcade.color.GREEN
        )

    def move_up(self):
        '''
        Moves the paddle up by increasing the y
        coordinate of the object.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.center.y += 10

    def move_down(self):
        '''
        Moves the paddle up by decreasing the y
        coordinate of the object.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.center.y -= 10