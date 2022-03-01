import pygame
import random


class Screen:

	def check_collision():
		if player.rect.colliderect(enemy):
			enemy.change_color(Color.blue)
			enemy.respawn()
			# player.respawn()
		if not player.rect.colliderect(enemy):
			enemy.change_color(Color.red)
		else:
			print("-----------------")

	def mainloop(loop):
		# when press left, right...
		if player.direction == 0: # left
			player.x -= speed
		elif player.direction == 2: # right
			player.x += speed
		elif player.direction == 1: # up
			player.y -= speed
		elif player.direction == 3: # down
			player.y += speed

		# get user event (press key...)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = 0
			elif event.type == pygame.KEYDOWN:

				# when you press left, right...
				'''	
                            u 1

				       l 0        2 r
                            
                            d 3

				'''
				if event.key == pygame.K_LEFT: # left = 0, right = 2, up = 1, down =3
					player.direction = 0
				elif event.key == pygame.K_RIGHT:
					player.direction = 2
				elif event.key == pygame.K_UP:
					player.direction = 1
				elif event.key == pygame.K_DOWN:
					player.direction = 3

			# when you release the key player stops
			elif event.type == pygame.KEYUP:
				player.direction = -1
		Screen.check_collision()
		pygame.display.update()
		clock.tick(60)
		return loop

class Color:
	yellow = (0, 255, 0)
	red = (255, 0, 0)
	blue = (0, 0, 255)

class Sprite:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.direction = -1
		self.image = pygame.Surface((50, 50))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect[0] = x
		self.rect[1] = y
		print(self.rect)

	def move_ai(self):

		# ESCAPE TO THE RIGHT ===========================
		if self.x < 580  and self.x > 0:
			# it will escape from right if the player is more to left
			if player.x < self.x:
				self.x += 3
			elif player.x > self.x:
				self.x -= 3
			else:
				if random.random() > 0.5:
					self.x += 3
				else:
					self.x -=3
			# if player.direction == 2: # if player goes right
			# 	self.x += 3 # self escapes right


		if self.y < 380 and self.y > 0:
			if player.y < self.y:
				self.y += 3
			elif player.y > self.y:
				self.y -= 3
			if random.random() > 0.5:
				self.y += 3
			else:
				self.y -= 3





	def change_color(self, color):
		self.image.fill(color)

	def draw(self):
		self.rect[0] = self.x
		self.rect[1] = self.y
		screen.blit(self.image, (self.x,self.y))

	def respawn(self):
		self.x = random.randrange(0, 580)
		self.y = random.randrange(0, 380)


pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

speed = 3




# =========== MAIN LOOP ==========
player = Sprite(0,0, Color.yellow)
enemy = Sprite(100,100, Color.red)
loop = 1
while loop:
	loop = Screen.mainloop(loop)
	screen.fill(0)
	player.draw()
	enemy.draw()
	enemy.move_ai()


pygame.quit()