import pygame
import random
import math

# initialization
pygame.init()

# display resolution
screen_res = (800, 600)
screen  = pygame.display.set_mode(screen_res)    

# title and icon
pygame.display.set_caption('AlienWare')
# pygame.display.set_icon()

# player variables
img_player = pygame.image.load("Img/Rocket.png")
player_x = screen_res[0]/2 - 32
player_y = screen_res[1] - 2*32
player_x_change = 0
enemy_x_chnage = 0

# player function
def player(x, y):
    screen.blit(img_player, (x, y))


# background
img_background = pygame.image.load("Img/Background.jpg")

# enemy variables
number_of_enemies = 6
img_enemy = pygame.image.load("Img/enemy.png")
enemy_x = random.randint(50, 700)
enemy_y = 100   
enemy_x_change = -0.2
enemy_y_change = 50

# enemy_function
def enemy(x,y):
    screen.blit(img_enemy, (x, y))
    # screen.blit(img_enemy, (x -0.2, y))

# bullet variables
img_bullet = pygame.image.load("Img/bullet.png")
bullet_x = player_x
bullet_y = player_y   
bullet_x_change = 0
bullet_y_change = 0
visible_bullet = False

# bullet_function
def bullet(x,y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x, y))
    # screen.blit(img_enemy, (x -0.2, y))

# score variable
score = 0

# detect collision
def detect_collision(bullet_pos, enemy_pos):
    global score
    determinant = math.sqrt(math.pow((bullet_pos[0] - enemy_pos[0]),2) + math.pow((bullet_pos[1] - enemy_pos[1]),2))
    if determinant < 25:
        print("collison detected")
        score +=1
        return True



isRunning = True
while isRunning:
    # screen.fill("purple")
    fired = False
    screen.blit(img_background, (0, 0))
   
    for event in pygame.event.get():
        # event close
        if event.type == pygame.QUIT:
            isRunning = False
        # event movement - arrow key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change -= 1
            if event.key == pygame.K_RIGHT:
                player_x_change += 1
            if event.key == pygame.K_UP:
                bullet_y_change = 0.5
                bullet_x = player_x
                bullet_y = player_y
                bullet(bullet_x, bullet_y)
                # visible_bullet = True
                # fired = True
                # bullet_y_change = 0
                  
            
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                player_x_change = 0
            # if (event.key == pygame.K_UP):


    #locating player            
    player_x += player_x_change

    #keep player inside screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= screen_res[0] - 64:
        player_x = screen_res[0] - 64

    player(player_x, player_y)
    
    # locating enemy
    enemy_x += enemy_x_change
    #keep enemy inside screen
    if enemy_x <= 0:
        print(enemy_x)
        enemy_x_change = + 0.2
        enemy_y += enemy_y_change 
        print(enemy_x)
        # enemy_y += enemy_y_change
    elif enemy_x >= screen_res[0] - 64:
         enemy_x_change = -0.2
         enemy_y += enemy_y_change 
    
    if enemy_y >= screen_res[1] - 2*32:
        print("Game Over")
    
    # bullet 
    # if fired:
    #     bullet_y_change = 0
    # bullet_y -= bullet_y_change 
    enemy(enemy_x, enemy_y)
    # bullet_x = player_x

    if visible_bullet: 
        bullet(bullet_x, bullet_y) # depends upon a button being pressed 
        bullet_y -= bullet_y_change 

    if bullet_y < 0:
            bullet(player_x, player_y)
            visible_bullet = False

    if detect_collision((bullet_x, bullet_y),(enemy_x, enemy_y)):
        print(score)     
                
    # Update the screen
    pygame.display.update()