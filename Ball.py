from Point import Point
from Velocity import Velocity

from random import randint, seed
import arcade

class Ball(object):
    '''
    Ball object that represents the ball moving on
    the screen of the game.
    '''
    
    center: Point
    velocity: Velocity

    def __init__(self):
        '''
        Initializes the object.
        '''
        seed()
        center_x: int = randint(150, 300)
        seed()
        center_y: int = randint(100, 100)
        seed()
        dx: int = 1
        seed()
        dy: int = 1
        self.center = Point(x=center_x, y=center_y)
        self.velocity = Velocity(dx=dx, dy=dy)

    def draw(self):
        '''
        Draws the circle on the screen at a random(ish)
        location.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        radius: int = 10
        arcade.draw_circle_outline(
            center_x=self.center.x, 
            center_y=self.center.y, 
            radius=radius, 
            color=arcade.color.GREEN
        )

    def advance(self):
        '''
        Moves the ball according to the velocity provided
        when it was initialized.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def bounce_horizontal(self):
        '''
        Reverses the x velocity of the ball

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.velocity.dx *= -1

    def bounce_vertical(self):
        '''
        Reverses the y velocity of the ball

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.velocity.dy *= -1

    def restart(self):
        '''
        Restarts the ball near the center of the map and 
        resets the velocity

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        seed()
        center_x: int = randint(150, 300)
        seed()
        center_y: int = randint(100, 100)
        seed()
        dx: int = 1
        seed()
        dy: int = 1
        self.center = Point(x=center_x, y=center_y)
        self.velocity = Velocity(dx=dx, dy=dy)