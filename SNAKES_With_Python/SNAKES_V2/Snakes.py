# Imports 
import pygame 
import sys
import random 
import GameObjects as game

# INITIALIZE PYGAME
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

eat_sound = pygame.mixer.music
eat_sound.load('eat_sound.wav')

score_font = pygame.font.SysFont("Arial", 15)
gameover_font = pygame.font.SysFont("Arial", 50) 
# score_font = pygame.font.Font.set_bold(score_font)
# Display window 
HEIGHT, WIDTH = 315, 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKES!")

def events(event, snake, game_over, food, tails, score):
	# Quit Game 
	if event.type == pygame.QUIT:
		sys.exit()
	# Restart Game
	if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
		game_over, food, snake, tails, score = restart()
		return game_over, food, snake, tails, score
	# KEY INPUTS 
	if event.type == pygame.KEYDOWN:
		# Check Direction of Snake
		if snake.direction == game.compast["1"]:
			# Change Direction
			if event.key == pygame.K_UP:
				snake.direction = game.compast["2"]
			elif event.key == pygame.K_DOWN:
				snake.direction = game.compast["4"]

		elif snake.direction == game.compast["2"]:
			if event.key == pygame.K_LEFT:
				snake.direction = game.compast["1"]
			elif event.key == pygame.K_RIGHT:
				snake.direction = game.compast["3"]

		elif snake.direction == game.compast["3"]:
			if event.key == pygame.K_UP:
				snake.direction = game.compast["2"]
			elif event.key == pygame.K_DOWN:
				snake.direction = game.compast["4"]
		else:
			if event.key == pygame.K_LEFT:
				snake.direction = game.compast["1"]
			elif event.key == pygame.K_RIGHT:
				snake.direction = game.compast["3"]
	return game_over, food, snake, tails, score

def randomize(w, h, size):
	return random.randint(0, 19) * 15, random.randint(0, 19) * 15 + 15

def graphics(obj, size):
	return pygame.draw.rect(window, obj.color, (obj.pos_x, obj.pos_y, size, size))

def draw_grid(window, w, h, c):
    for hor in range(0, 315, 15):
        pygame.draw.line(window, c, (0, hor), (w, hor))
    for ver in range(0, 300, 15):
        pygame.draw.line(window, c, (ver, 15), (ver, h))

def restart():
	game_over = False
	food = None
	snake_x, snake_y = randomize(WIDTH, HEIGHT, size)
	snake = game.SnakeHead(snake_x, snake_y)
	tails = []
	score = 0
	return game_over, food, snake, tails, score

def draw_texts(score, gameover):
	if gameover:
		gameover_text = gameover_font.render('GAME OVER' , 1, (0,255,0))
		fin_score = gameover_font.render('SCORE: ' + str(score) , 1, (0,255,0))
		window.blit(gameover_text, (15, 100))
		window.blit(fin_score, (15, 150))
	else:
		score_text =  score_font.render('Score: ' + str(score) + '                R/r = Restart' , 1, (0,255,0))
		window.blit(score_text, (5, 0))

size = 15
run = True

# INITIATE GAME
game_over, food, snake, tails, score = restart()
while run:
	window.fill((0,0,0))
	# Ingame
	if not game_over:
		# Spawn Food
		while food == None:
			food_x, food_y = randomize(WIDTH, HEIGHT, size)
			if game.SnakeFood(food_x,food_y).validate(food, tails):
				food = game.SnakeFood(food_x,food_y)
				break
		g_food = graphics(food, size)
	

		# Snake
		last = [snake.pos_x, snake.pos_y]
		snake.move()
		g_tails = []
		for tail in range(len(tails)):
			last = game.update_tail(tails, tail, last)
			t = graphics(tails[tail], size)
			g_tails.append(t)	
		g_snake = graphics(snake, size)
		
		# Check Collision
		if snake.wall_collide(HEIGHT,WIDTH) or snake.tail_collide(g_tails, g_snake):
			game_over = True

		# Snake Eating
		if g_food.colliderect(g_snake):
			tails.append(game.SnakeTail(food.pos_x, food.pos_y))
			score = snake.eat(score)
			eat_sound.play()
			food = None

	for event in pygame.event.get():
		game_over, food, snake, tails, score = events(event, snake, game_over, food, tails, score)

	draw_grid(window, WIDTH, HEIGHT, (0,0,0))
	draw_texts(score, game_over)
	clock.tick(5)
	pygame.display.update()