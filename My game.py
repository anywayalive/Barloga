

# import pygame
# pygame.init()
# gameDisplay = pygame.display.set_mode((800,600))
# pygame.display.set_caption(‘My first game’)
# clock = pygame.time.Clock(60)
# # Loop until the user clicks the close button.
# done = False
# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()
	
# # -------- Main Program Loop -----------
# while not done:
# 	# --- Main event loop
# 	for event in pygame.event.get(): # User did something
# 		if event.type == pygame.QUIT: # If user clicked close
# 		done = True # Flag that we are done so we exit this loop
	
# 	# --- Game logic should go here
# 	# --- Drawing code should go here
# 	# First, clear the screen to white. Don't put other drawing commands
# 	# above this, or they will be erased with this command.
# 	screen.fill(WHITE)
# 	# --- Go ahead and update the screen with what we've drawn.
# 	pygame.display.update()
# 	# --- Limit to 60 frames per second
# 	clock.tick(60)

# pylint: disable=C0321 


# /////////////////////////////////////////////////////////////////////////////

# import pygame

# pygame.init()

# WHITE = (255, 255, 255)	
# ORANGE = (255, 150, 100)

# DISPLAY_WIDTH = 400 
# DISPLAY_HEIGH = 400 

# gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

# pygame.display.set_caption("My first game")

# clock=pygame.time.Clock()

# # Loop until the user clicks the close button.
# done = False

# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()

# # -------- Main Program Loop -----------
# while not done:
# 	# --- Main event loop
# 	for event in pygame.event.get(): # User did something
# 		if event.type == pygame.QUIT: # If user clicked close
# 		    done = True # Flag that we are done so we exit this loop
	
# 	# --- Game logic should go here
# 	# --- Drawing code should go here
# 	# First, clear the screen to white. Don't put other 
# 	# drawing commands above this, 
# 	# or they will be erased with this command.
	
# 	gameDisplay.fill(ORANGE)
	
# 	# --- Go ahead and update the screen with what we've drawn.
# 	pygame.display.update()
	
# 	# --- Limit to 60 frames per second
# 	clock.tick(60)

# //////////////////////////////////////////////////////////////

# import pygame
# pygame.init()
# gameDisplay=pygame.display.set_mode((400,300))
# pygame.display.set_caption("My first game")
# clock=pygame.time.Clock()
# crashed=False
# while not crashed:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print("User asked to quit.")
#         elif event.type == pygame.KEYDOWN:
#             print("User pressed a key.")
#         elif event.type == pygame.KEYUP:
#             print("User let go of a key.")
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print("User pressed a mouse button")

        
#     pygame.display.update()

#     clock.tick(60)

# pygame.quit()
# #quit()

# //////////////////////////////////////////////////////////

# #pylint: disable=C0321 
# import pygame
# x=50
# y=50
# width=40
# height=60
# vol=30
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("My first game")

# #clock = pygame.time.Clock()

# done = False
# clock = pygame.time.Clock()

# while not done:
#     pygame.time.delay(100)

#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
#     keys=pygame.key.get_pressed()
    
#     if keys[pygame.K_LEFT] and x>vol:
#         x=x-vol
#     if keys[pygame.K_RIGHT] and x<500-vol-width:
#         x=x+vol
#     if keys[pygame.K_UP] and y>vol:
#         y=y-vol
#     if keys[pygame.K_DOWN] and y<500-vol-height:
#         y=y+vol
#     screen.fill((0,0,0))
#     pygame.draw.rect(screen, (255,0,0), [x, y, width, height])
       
#     pygame.display.update()
# 	# clock.tick(60)

# /////////////////////////////////////////////////////////

import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Fly')
 
clock = pygame.time.Clock()

#обновляємо екран 
pygame.display.update()
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("D:\Lectures\My_lect_Python\Game\+\player.png").convert()

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
 
    
# Get the current mouse position. This returns the position
    # as a list of two numbers.
#повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
#копіює картинку на екран
    screen.blit(player_image, [x, y])
 
#обновляємо екран
    pygame.display.flip()
 
    clock.tick(60)


pygame.quit()