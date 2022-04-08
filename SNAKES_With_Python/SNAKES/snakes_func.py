import pygame
import random
# ===============================================================================
# CLASSES
class box:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

# IN-GAME EVENTS AND FUNCTIONS
def draw_grid(window, w, h, c):
    for hor in range(0, 630, 30):
        pygame.draw.line(window, c, (0, hor), (w, hor))
    for ver in range(0, 600, 30):
        pygame.draw.line(window, c, (ver, 30), (ver, h))


def move(snake, dir):
    pos = [snake.x, snake.y]
    if dir[0]:
        pos[0] -= 30
        if pos[0] < 0:
            pos[0] = 570
        return pos
    elif dir[1]:
        pos[1] -= 30
        if pos[1] < 30:
            pos[1] = 600
        return pos
    elif dir[2]:
        pos[0] += 30
        if pos[0] > 570:
            pos[0] = 0
        return pos
    else:
        pos[1] += 30
        if pos[1] > 600:
            pos[1] = 30
        return pos


def eat(snake, food, speed, score, tails, BLUE):
    sound = False
    if snake.x == food.x and snake.y == food.y:
        speed += 0.2
        score += 1
        tails.append(box(BLUE, food.x, food.y))
        food.x, food.y = random.randint(1, 19) * 30, random.randint(2, 19) * 30
        sound = True
    return speed, score, tails, sound


def update_tail_pos(tails, tail, last):
    last_ctr = [tails[tail].x, tails[tail].y]
    tails[tail].x = last[0]
    tails[tail].y = last[1]
    return last_ctr


def collision(snake, tails):
    for i in range(2, len(tails)):
        if tails[i].x == snake.x and tails[i].y == snake.y:
            return True
    return False

def start():
    return 0, 5, [], False