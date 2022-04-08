# SNAKE GAME
import pygame
import sys
import random
import snakes_func as f

# INITIALIZE PYGAME
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
pygame.display.set_caption("SNAKES!")
# ===============================================================================
# INITIALIZE VALUES
my_font = pygame.font.SysFont("monospace", 30)
eat_sound = pygame.mixer.music
eat_sound.load('eat_sound.wav')

# Color
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)

HEIGHT, WIDTH = 630, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
BOX_SIZE = 30

food_x, food_y = random.randint(1, 19) * 30, random.randint(2, 19) * 30
food = f.box(RED, food_x, food_y)

snake = f.box(BLUE, 300, 330)

run = True
frame = 0

score, speed, tails, over = f.start()
direction = [False, False, True, False]

# MAIN GAME RUN 
while run:
    frame += 1
    window.fill(SILVER)
    # f.draw_grid(window, WIDTH, HEIGHT, WHITE)
    if len(tails) > 0:
        last = [snake.x, snake.y]
        for tail in range(len(tails)):
            last = f.update_tail_pos(tails, tail, last)
            pygame.draw.rect(window, tails[tail].color, (tails[tail].x, tails[tail].y, BOX_SIZE, BOX_SIZE))

    if (not over):
        pos = f.move(snake, direction)
        snake.x = pos[0]
        snake.y = pos[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction[2] == False:
                direction = [True, False, False, False]
            elif event.key == pygame.K_UP and direction[3] == False:
                direction = [False, True, False, False]
            elif event.key == pygame.K_RIGHT and direction[0] == False:
                direction = [False, False, True, False]
            elif event.key == pygame.K_DOWN and direction[1] == False:
                direction = [False, False, False, True]
            elif event.key == pygame.K_r:
                score, speed, tails, over = f.start()

    pygame.draw.rect(window, food.color, (food.x, food.y, BOX_SIZE, BOX_SIZE))
    pygame.draw.rect(window, snake.color, (snake.x, snake.y, BOX_SIZE, BOX_SIZE))
    

    over = f.collision(snake, tails)
    speed, score, tails, sound = f.eat(snake, food, speed, score, tails, BLUE)
    if sound:
        eat_sound.play()
    # UI
    text = "SCORE: " + str(score) + "       Restart = r"
    score_text = my_font.render(text, 1, BLACK)
    window.blit(score_text, (50, 0))

    clock.tick(speed)
    pygame.display.update()

# BY REYES EUGENE