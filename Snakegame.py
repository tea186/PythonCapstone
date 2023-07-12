import pygame
import time
import random

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
purple = pygame.Color(240, 0, 255)
blue_green = pygame.Color(0, 255, 170)
forest_green = pygame.Color(0, 50, 0)
yellow = pygame.Color(255, 255, 0)


# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# food position
food_position = [random.randrange(1, (window_x // 20)) * 20,
                  random.randrange(1, (window_y // 20)) * 20]

food_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# Timer
start_time = time.time()
end_time = 0

# Load high score from file
def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    return high_score

# Save high score to file
def save_high_score(high_score):
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))

# displaying Score and Timer function
def show_score(color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    # displaying text
    game_window.blit(score_surface, score_rect)
    # displaying timer
    timer_surface = score_font.render('Timer : ' + str(int(time.time() - start_time)) + 's', True, color)
    timer_rect = timer_surface.get_rect()
    timer_rect.topright = (window_x - 10, 10)
    game_window.blit(timer_surface, timer_rect)

# game over function
def game_over():
    global score, start_time
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, blue_green)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x // 2, window_y // 4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)

    # Display end time and high score
    End_time = time.time()
    high_score = load_high_score()

    end_time_surface = my_font.render('Time : ' + str(int(End_time - start_time)) + 's', True, purple)
    high_score_surface = my_font.render('High Score : ' + str(high_score), True, blue_green)

    end_time_rect = end_time_surface.get_rect()
    high_score_rect = high_score_surface.get_rect()

    end_time_rect.midtop = (window_x // 2, window_y // 2)
    high_score_rect.midtop = (window_x // 2, window_y // 2 + 50)

    game_window.blit(end_time_surface, end_time_rect)
    game_window.blit(high_score_surface, high_score_rect)

    pygame.display.flip()

    # Save new high score if achieved
    if score > high_score:
        high_score = score
        save_high_score(high_score)

    # After 5 seconds, quit the program
    time.sleep(5)
    pygame.quit()
    quit()

# Main Function
while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 20
    if direction == 'DOWN':
        snake_position[1] += 20
    if direction == 'LEFT':
        snake_position[0] -= 20
    if direction == 'RIGHT':
        snake_position[0] += 20

    # Snake body growing mechanism
    # if food and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    # noinspection PyChainedComparisons
    if (snake_position[0] >= food_position[0] and
        snake_position[0] < food_position[0] + 20 and
        snake_position[1] >= food_position[1] and
        snake_position[1] < food_position[1] + 20):
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_position = [random.randrange(1, (window_x // 20)) * 20,
                          random.randrange(1, (window_y // 20)) * 20]

    food_spawn = True
    game_window.fill(forest_green)

    for pos in snake_body:
        pygame.draw.rect(game_window, yellow,
                         pygame.Rect(pos[0], pos[1], 20, 20))
    pygame.draw.rect(game_window, red, pygame.Rect(
        food_position[0], food_position[1], 20, 20))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 20:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 20:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
