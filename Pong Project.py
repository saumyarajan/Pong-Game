import pygame
pygame.init()

# Define some colors
BLACK = (0,0,0) # Black in hexadecimal is #000000
WHITE = (255,255,255) # White in hexadecimal is #FFFFFF

class Rectangle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carry_on = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

line_pos = 349
ball_speed_x = 2
ball_speed_y = 2

# Drawing the left paddle
left_paddle = Rectangle(WHITE, 10, 100)
left_paddle.rect.x = 20
left_paddle.rect.y = 200

# Drawing the right paddle
right_paddle = Rectangle(WHITE, 10, 100)
right_paddle.rect.x = 670
right_paddle.rect.y = 200

# Drawing the ball
ball = Rectangle(WHITE, 10, 10)
ball.rect.x = line_pos
ball.rect.y = 245

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(left_paddle)
all_sprites_list.add(right_paddle)
all_sprites_list.add(ball)

left_score = 0
right_score = 0

while carry_on:
    for event in pygame.event.get(): # User did something
       if event.type == pygame.QUIT: # If user clicked close
           print("User clicked QUIT")
           carry_on = False # Flag that we are done so we exit this loop

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: # left paddle moves up
        print("W is pressed")
        left_paddle.rect.y -= 5
    if keys[pygame.K_s]: # left paddle moves down
        print("S is pressed")
        left_paddle.rect.y += 5

    # This code allows player to control the right paddle
    if keys[pygame.K_UP]: # right paddle moves up
        print("Up is pressed")
        right_paddle.rect.y -= 5
    if keys[pygame.K_DOWN]: #right paddle moves down
        print("Down is pressed")
        right_paddle.rect.y += 5

    # This code controls the right paddle automatically
    # right_paddle.rect.y = ball.rect.y - 50

    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y
    if ball.rect.y >= 500: # if ball is at bottom
        ball_speed_y = -ball_speed_y
    if ball.rect.y <= 0: # if ball is at top
        ball_speed_y = -ball_speed_y
    if ball.rect.x >= 700: # if ball is at right, reset to center
        ball.rect.x = line_pos
        ball.rect.y = 245
        left_score += 1
    if ball.rect.x <= 0: # if ball is at left, reset to center
        ball.rect.x = line_pos
        ball.rect.y = 245
        right_score += 1

    if ((ball.rect.y >= left_paddle.rect.y) and (ball.rect.y <= (left_paddle.rect.y + 100)) and ball.rect.x < 30): # hits the left paddle
        ball_speed_x = -ball_speed_x
    if ((ball.rect.y >= right_paddle.rect.y) and (ball.rect.y <= (right_paddle.rect.y + 100)) and ball.rect.x > 670): # hits the right paddle
        ball_speed_x = -ball_speed_x
        
    all_sprites_list.update()
    
    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [line_pos, 0], [line_pos, 500], 5)

    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(left_score), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(right_score), 1, WHITE)
    screen.blit(text, (420,10))
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
    
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
