import pygame

class ScrabbleBoard:
    
    # location of scrabble board within board
    TOP_X = 0
    TOP_Y = 0
    BOTTOM_X = 600
    BOTTOM_Y = 600

    # number of rows and columns on the scrabble board
    NUM_BOARD_ROWS = 15
    NUM_BOARD_COLS = 15

    # height and width of each square
    BOARD_CELL_HEIGHT = 40
    BOARD_CERLL_WIDTH = 40

    # constructor - load the screen and the image    
    def __init__(self, screen):
        self.screen = screen
        self.board = pygame.image.load("scrabble_board.jpg")

    # update the board with the correct content
    def update(self):
        self.screen.blit(self.board, (self.TOP_X, self.TOP_Y))
        pygame.display.update()

    # returns true if the pos is within bounds of the board, else retuns false
    def is_point_in_bounds(self, pos):
        # Aarav to implement
        pass

    # map the position to the actual square in which the user has clicked; returns identifier of the square as (row, col)
    # if it is not a valid square, return (-1, -1)
    def get_square(self, pos):
        # Aarav to implement
        pass


    