from Pong import Pong
import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300 

def main():
    '''
    Begins the pong game
    '''
    window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()