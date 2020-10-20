import arcade
import random
from Point import Point
from Velocity import Velocity
from Ball import Ball
from Paddle import Paddle

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

class Pong(arcade.Window):
    '''
    Classic pong arcade game but with only one player. 
    Focuses on keeping the ball on the right side.
    '''
    ball: Ball
    paddle: Paddle
    score: int
    holding_up: bool
    holding_down: bool

    def __init__(self, width, height):
        '''
        Init function begins the frame window and sets up the default values

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.holding_up = False
        self.holding_down = False

        arcade.set_background_color(arcade.color.BLACK)
    
    def on_draw(self):
        '''
        Function called automatically by the framework to render the game.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        arcade.start_render()
        self.ball.draw()
        self.paddle.draw()
        self.draw_score()
        self.draw_ball_position()
        self.draw_paddle_position()

    def draw_score(self):
        '''
        Draws the score of the player on the top left corner
        of the window.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        score_text = f"Score: {self.score}"
        x: int = 10
        y: int =  280
        arcade.draw_text(
            text=score_text,
            start_x=x,
            start_y=y,
            font_size=12,
            color=arcade.color.GREEN
        )

    def draw_ball_position(self):
        '''
        Draws the position of the ball on the top right of the screen

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        x: int = self.ball.center.x
        y: int = self.ball.center.y
        text: str = f"Ball [X: {x} Y: {y}]"
        arcade.draw_text(
            text=text,
            start_x=280,
            start_y=280,
            font_size=12,
            color=arcade.color.GREEN
        )

    def draw_paddle_position(self):
        '''
        Draws the position of the paddle on the bottom right of the screen

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        x: int = self.paddle.center.x
        y: int = self.paddle.center.y
        text: str = f"Paddle [X: {x} Y: {y}]"
        arcade.draw_text(
            text=text,
            start_x=270,
            start_y=10,
            font_size=12,
            color=arcade.color.GREEN
        )

    def update(self, delta_time):
        '''
        Updates the screen based on the new values

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.ball.advance()
        self.check_keys()
        self.check_miss()
        self.check_hit()
        self.check_bounce()
    
    def check_bounce(self):
        '''
        Checks to see if the ball is within the boundaries that it needs.
        If the ball is too close to the right or left side then it will
        reverse the delta_x of the ball. If the ball is too far up or
        down then it will reverse the delta_y of the ball.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.ball.center.x < 0:
            self.ball.bounce_horizontal()

        if self.ball.center.x > 400:
            self.ball.bounce_horizontal()

        if self.ball.center.y < 0:
            self.ball.bounce_vertical()

        if self.ball.center.y > 300:
            self.ball.bounce_vertical()
    
    def check_miss(self):
        '''
        Checks to see if the ball has gone too far to the left, meaning
        that the player missed the ball.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.ball.center.x < 0:
            self.score -= SCORE_MISS
            self.ball.restart()
    
    def check_hit(self):
        '''
        Check to see if the ball has hit the paddle on the x or
        y plane of the paddle.

        If it hits, it will increment the velocity by 1 and
        increase the score.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        too_close_x: int = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y: int = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        ball_x: int = self.ball.center.x
        ball_y: int = self.ball.center.y
        paddle_x: int = self.paddle.center.x
        paddle_y: int = self.paddle.center.y

        if (abs(ball_x - paddle_x) < too_close_x and
            abs(ball_y - paddle_y) < too_close_y):
            self.ball.bounce_horizontal()
            self.score += SCORE_HIT
            self.ball.velocity.dx += 1
            self.ball.velocity.dy += 1

    def check_keys(self):
        '''
        Checks if the up or down keys are being held down.
        If they are being held down, then move the paddle
        until it cannot move any further.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        paddle_y: int = self.paddle.center.y
        upper_edge: int = SCREEN_HEIGHT - (PADDLE_HEIGHT / 2) - 5
        if self.holding_up and paddle_y < upper_edge:
            self.paddle.move_up()

        if self.holding_down and paddle_y > 30: 
            self.paddle.move_down()
    
    def on_key_press(self, key, key_modifers):
        '''
        Detects if the key is being pressed, updates
        values accordingly.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if key == arcade.key.UP or key == arcade.key.W:
            self.holding_up = True
        
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.holding_down = True
    
    def on_key_release(self, key, key_modifers):
        '''
        Checks to see if the key has been released, and if it
        has then it will disengage the button.

        Parameters
        ----------
        None

        Returns
        -------
        None 
        '''
        if key == arcade.key.UP or key == arcade.key.W:
            self.holding_up = False
        
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.holding_down = False
