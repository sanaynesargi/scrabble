# import the pygame module, so you can use it
import pygame
import boards

 
def main():
    # initialize the pygame module
    pygame.init()
   
    # load and set the logo for the main page
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("SCRABBLE")

    # create the master screen of size 600 X 600
    # currently includes only scrabble board but will increase later
    screen = pygame.display.set_mode((800,800))    
     
    # create the object for the scrabble board and draw it
    scrabble_board = boards.ScrabbleBoard(screen)
    scrabble_board.update()

    # pygame Event Loop

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

            #
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get position
                print(event.pos)
                if (scrabble_board.is_point_in_bounds(event.pos)):
                    print("In Scrabble Board")
                    print(scrabble_board.get_square(event.pos))
                else:
                    print("Outside Scrabble Board")
                    
            if event.type == pygame.MOUSEBUTTONUP:
                # get position
                print(event.pos)
                if (scrabble_board.is_point_in_bounds(event.pos)):
                    print("In Scrabble Board")
                    print(scrabble_board.get_square(event.pos))
                else:
                    print("Outside Scrabble Board")
    
if __name__=="__main__":
    # call the main function
    main()
           
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()