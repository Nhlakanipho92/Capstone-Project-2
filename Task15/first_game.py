# Import the pygame library.
# Import random to generate random numbers.
import pygame
import random
# Initialize the pygame modules. 
pygame.init() 
# Sets the size of the screen by width and height.
screen_width = 1040
screen_height = 680
# Colour of the text object.
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# Font for text object.
font = pygame.font.Font("freesansbold.ttf", 32)
# The position in the screen.
X = 400
Y = 400
# This function creates a text event you win.
def show_win(x, y):
    text = font.render("You Win !!", True, green, blue)
    screen.blit(text, (x,y))
# This function creates a text event you lose.
def show_lose(x, y):
    text = font.render("You lose !!", True, green, blue)
    screen.blit(text, (x,y))

# Displays caption at the top of the page.
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nhlakanipho first game. ")

# Characters are loaded.
player = pygame.image.load("image.png")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("enemy.png")
enemy3 = pygame.image.load("enemy.png")
prize = pygame.image.load("prize.jpg")

# Ensure the images are in boundary and can be detected.
image_WIDTH = player.get_height()
image_HEIGHT = player.get_width()
enemy1_WIDTH = enemy1.get_height()
enemy1_HEIGHT = enemy1.get_width()
enemy2_WIDTH = enemy2.get_height()
enemy2_HEIGHT = enemy2.get_width()
enemy3_WIDTH = enemy3.get_height()
enemy3_HEIGHT = enemy3.get_width()
prize_WIDTH = prize.get_height()
prize_HEIGHT = prize.get_width()

# Sets the position of the player on the X and Y.
playerXPosition = 100
playerYPosition = 50

# Declares the changes that player makes and sets them to 0.
playerXPosition_change = 0
playerYPosition_change = 0

# Declare the enemys position and places the enemy in a random position.
enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_HEIGHT)
enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_HEIGHT)
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_HEIGHT)
# Declares the prize position and places the prize in a random position.
prizeXPosition =  screen_width
prizeYPosition =  random.randint(0, screen_height - enemy3_HEIGHT)

# LOOP the game.
# Running throught all the condition and repeats if true.
# Rendering is done here.
while 1: 
# The characters of the game are drawn using blit and positioned.
    screen.fill(0)
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

# This function updates the screen.
    pygame.display.flip()
# This are events are looped in the game. 
    for event in pygame.event.get():
# Event checks if user quits the game if not runs the other events.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
# If the the event is pass the player will move
# If player moves left the event will run.
# If player moves right the will run. 
# The player will away from the y at 15 loops.
# Th player towards the y at 15 loops.
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT: 
                playerXPosition_change -= 16
            if event.key == pygame.K_RIGHT:
                playerXPosition_change += 16
                
# If there is no event player stop moving.
# If 0 means no move or looping of the player.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
               playerXPosition_change = 0
            if event.key == pygame.K_RIGHT:
               playerXPosition_change = 0
# If the the event is pass the player will move
# If player moves up the event will run.
# If player moves down the will run. 
# The player will away from the y at 15 loops.
# Th player towards the y at 15 loops.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                playerYPosition_change -= 16
            if event.key == pygame.K_DOWN:
                playerYPosition_change  = 16
# If there is no event player stop moving.
# If 0 means no move or looping of the player.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: 
                playerYPosition_change = 0
            if event.key == pygame.K_DOWN:
                playerYPosition_change = 0
# Increase change made by key event by 15.
# Than refreshs the position.
        playerXPosition += playerXPosition_change
        playerYPosition += playerYPosition_change
# Creates a boundary box for player.
    playerBox = pygame.Rect(player.get_rect())
   
# Check for collision with enemy on player.
    playerBox.top = playerYPosition
    playerBox.bottom = playerYPosition
    playerBox.left = playerXPosition
    playerBox.right = playerXPosition
#Bounding box for the enemy.   
    enemyBox = pygame.Rect(enemy1.get_rect())
    enemyBox = pygame.Rect(enemy2.get_rect())
    enemyBox = pygame.Rect(enemy3.get_rect())
# Bounding box for prize.
    prizeBox = pygame.Rect(prize.get_rect())
# Check for collision with player.
    enemyBox.top = enemy1YPosition
    enemyBox.bottom = enemy1YPosition
    enemyBox.right = enemy1XPosition
    enemyBox.left = enemy1XPosition
    enemyBox.top = enemy2YPosition
    enemyBox.bottom = enemy2YPosition
    enemyBox.right = enemy2XPosition
    enemyBox.left = enemy2XPosition
    enemyBox.top = enemy3YPosition
    enemyBox.bottom = enemy3YPosition
    enemyBox.right = enemy3XPosition
    enemyBox.left = enemy3XPosition

    prizeBox.top = prizeYPosition
    prizeBox.bottom = prizeYPosition
    prizeBox.right = prizeXPosition
    prizeBox.left = prizeXPosition
   
# Test collision of the boxes.
# If collides with ememy you lose is displayed for 5 sec.
# Game ends.
    if playerBox.colliderect(enemyBox):    
        show_lose(X, Y)    
        pygame.display.update()
        pygame.time.delay(5000)
# prints you lose.  
        print ("You lost!")
        pygame.quit()
        exit(0)

# Test collision of the boxes.
# If collides with prize you Win is displayed for 5 sec.
# Game ends.
    if playerBox.colliderect(prizeBox):    
        show_win(X, Y)    
        pygame.display.update()
        pygame.time.delay(5000)
# prints you win.  
        print ("You Win!")
        pygame.quit()
        exit(0)

# Make enemy approach the player.
    enemy1XPosition -= 0.18
    enemy2XPosition -= 0.22
    enemy3XPosition -= 0.15
# Makes the praze approach the player.
    prizeXPosition  -= 0.06

# GAME OVER 
# NHLAKANIPH HLOPHE 
# nhlakaniphohlophe@gmail.com
    
    
   
  
