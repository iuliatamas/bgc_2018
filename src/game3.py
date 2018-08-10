import pygame
import time

class GameState():
    quit = False

    # Define some colors we want to use
    black = (0,0,0)
    white = (255,255,255)

    # Define how big our game sreen should be
    display_width = 800
    display_height = 600

    clock = pygame.time.Clock()

    birdImage = pygame.image.load('yellow-bird.png')
    treeImage = pygame.image.load("hearts-tree.png")
    bird_x =  0
    bird_y = 0

state = GameState()

def display_tree_at(x, y):
    state.gameDisplay.blit(state.treeImage, (x,y))

def display_bird_at(x, y):
    state.gameDisplay.blit(state.birdImage, (x,y))

def clear_screen():
    state.gameDisplay.fill(state.white)
    display_tree_at(0, 100)
    display_tree_at(100, 200)
    display_tree_at(200, 300)
    display_tree_at(300, 400)

    display_tree_at(400, 100)
    display_tree_at(500, 200)
    display_tree_at(600, 300)
    display_tree_at(700, 400)

def init_game():
    pygame.init()

    state.gameDisplay = pygame.display.set_mode((state.display_width, state.display_height))
    pygame.display.set_caption('Birdzzz')

def play_game():
    L = pygame.USEREVENT
    R = pygame.USEREVENT + 1
    U = pygame.USEREVENT + 2
    D = pygame.USEREVENT + 3

    fixed_events = [R, D, R, D, R, D, R, D, R, D, R, D]
    delay = 200

    for event in fixed_events:
        pygame.time.set_timer(event, delay)
        delay += 200

    while not state.quit:
        bird_x_change = 0
        bird_y_change = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.quit = True
            elif event.type == L:
                bird_x_change = -5
            elif event.type == R:
                bird_x_change = 5
            elif event.type == U:
                bird_y_change = -5
            elif event.type == D:
                bird_y_change = 5

        state.bird_x += bird_x_change
        state.bird_y += bird_y_change

        clear_screen()
        display_bird_at(state.bird_x, state.bird_y)
        pygame.display.update()


init_game()
play_game()

pygame.quit()
quit()
