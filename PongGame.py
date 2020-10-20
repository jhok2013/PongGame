from random import randint, seed
import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

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
       
def main():
    '''
    Begins the pong game
    '''
    window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()      