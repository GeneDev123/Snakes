import random 
import pygame
compast = { #1EAST,2NORTH,3WEST,4SOUTH
	"1": (1,0,0,0), "2": (0,1,0,0),
	"3": (0,0,1,0), "4": (0,0,0,1)
}
colors = {
	"white": (255, 255, 255), "blue": (0, 0, 255),
	"red": (255, 0, 0), "green": (0, 255, 0),
	"black": (0, 0, 0)
} 

class GameObject:
	def __init__(self, pos_x, pos_y):
		self.pos_x = pos_x 
		self.pos_y = pos_y

class SnakeHead(GameObject):
	direction = compast[str(random.randint(1,4))] 	
	color = colors["blue"]
	
	def move(self):
		if self.direction == (1,0,0,0):
			self.pos_x = self.pos_x - 15  
		elif self.direction == (0,1,0,0):
			self.pos_y = self.pos_y - 15
		elif self.direction == (0,0,1,0):
			self.pos_x = self.pos_x + 15
		elif self.direction == (0,0,0,1):
			self.pos_y = self.pos_y + 15
	
	def wall_collide(self, h, w):
		if self.pos_x < 0 or self.pos_x > w:
			return True
		elif self.pos_y < 15 or self.pos_y > h:
			return True
		else: 
			return False  

	def tail_collide(self, tails, snake):
		for i in tails:
			if i.colliderect(snake):
				return True
		return False

	def eat(self, score):
		score +=1
		return  score

class SnakeTail(GameObject):
	color = colors["green"]

def update_tail(tails, tail, last):
	last_ctr = [tails[tail].pos_x, tails[tail].pos_y]
	tails[tail].pos_x = last[0]
	tails[tail].pos_y = last[1]
	return last_ctr
	
class SnakeFood(GameObject):	
	color = colors["red"]
	def validate(self, food, tails):
		# Check there is already food and if overlapped with the tails
		for i in tails:
			if i.pos_x == self.pos_x and i.pos_y == self.pos_y:
				return False  
		if food != None:
			return False 
		else:
			return True