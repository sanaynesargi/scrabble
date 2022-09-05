import pygame

class ScrabbleBoard:
    
    #location of scrabble board within board
    top_x = 0
    top_y = 0

    # constructor - load the screen and the image    
    def __init__(self, screen):
        self.screen = screen
        self.board = pygame.image.load("scrabble_board.jpg")

    # update the board with the correct content
    def update(self):
        self.screen.blit(self.board, (self.top_x, self.top_y))
        pygame.display.update()

    