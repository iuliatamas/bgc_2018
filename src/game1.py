import pygame

class GameState():
    quit = False

    # Define some colors we want to use
    black = (0,0,0)
    white = (255,255,255)

    # Define how big our game screen should be
    display_width = 800
    display_height = 600

    birdImage = pygame.image.load('green-bird.png')
    bird_x =  0
    bird_y = 0

state = GameState()

def display_bird_at(x,y):
    state.gameDisplay.blit(state.birdImage, (x,y))

def init_game():
    pygame.init()

    state.gameDisplay = pygame.display.set_mode((state.display_width, state.display_height))
    pygame.display.set_caption('Birdzzz')

def play_game():
    while not state.quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.quit = True

            bird_x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bird_x_change = -5


        state.bird_x += bird_x_change

        state.gameDisplay.fill(state.white)
        display_bird_at(state.bird_x, state.bird_y)
        pygame.display.update()


init_game()
play_game()

pygame.quit()
quit()