"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
import math

 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
class Game():
    # Initialize Pygame
    pygame.init()
     
    # Set the height and width of the screen
    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])


# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
class BlockList():
    block_list = pygame.sprite.Group()
     
    # This is a list of every sprite. 
    # All blocks and the player block as well.
    all_sprites = pygame.sprite.Group()


    # Creates 50 blocks and put it into block_list and all_sprites_list
    for i in range(50):
        # This represents a block
        block = Block(BLACK, 20, 15)
     
        # Set a random location for the block
        block.rect.x = random.randrange(Game.screen_width)
        block.rect.y = random.randrange(Game.screen_height)
     
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites.add(block)
 
# Create a RED player block and put it in all_sprites list
player = Block(RED, 20, 15)
BlockList.all_sprites.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0


# -------- Main Program Loop -----------
vec = pygame.math.Vector2
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Clear the screen
    Game.screen.fill(WHITE)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x, player.rect.y = vec(pos[0], pos[1])
    # player.rect.y = pos[1]
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, BlockList.block, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
 
    # Draw all the sprites
    BlockList.all_sprites.draw(Game.screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()