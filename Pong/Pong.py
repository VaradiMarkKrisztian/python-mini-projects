import pygame

def p1_input(key_pressed,p1):
    if key_pressed[pygame.K_w] and p1.y - velocity >=0 :
        p1.y -= velocity
    elif key_pressed[pygame.K_s] and p1.y + velocity + p1.height <= screen.get_height():
        p1.y += velocity
def p2_input(key_pressed,p2):
    if key_pressed[pygame.K_UP] and p2.y - velocity >=0:
        p2.y -= velocity
    elif key_pressed[pygame.K_DOWN] and p2.y + velocity + p2.height <= screen.get_height():
        p2.y += velocity

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Pong")
text_font = pygame.font.Font('Font/Pixeltype.ttf',50)
game_active = True
score = [0,0] #score of the 2 players
clock = pygame.time.Clock()

player1 = pygame.image.load("Graphics/Player.png").convert_alpha()
player2 = pygame.image.load("Graphics/Player.png").convert_alpha()
player_rect1 = player1.get_rect(center = (20,200))
player_rect2 = player2.get_rect(center = (780,200))
move_speed_player1 = 0
move_speed_player2 = 0
velocity = 5
ball_vel_x= -4
ball_vel_y = -4

ball = pygame.image.load("Graphics/Ball.png").convert_alpha()
ball_rect = ball.get_rect(center =(200,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        if game_active == False:
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                ball_rect.x = 400
                ball_rect.y = 200
                game_active = True
            

    if game_active == True:
        screen.fill((34,39,102))
        screen.blit(player1,player_rect1)
        screen.blit(player2,player_rect2)    
        Score_surface = text_font.render(f'{score[0]} : {score[1]}', False, (101,102,120))
        score_rect = Score_surface.get_rect(center = (400,25))
        screen.blit(Score_surface,score_rect)
        screen.blit(ball,ball_rect)
        
        #ball movement
        # for collision to be avoided the ball needs to be inside x = 0, 800 and y= 0,400
        ball_rect.x = ball_rect.x + ball_vel_x
        ball_rect.y = ball_rect.y + ball_vel_y
        #if (ball_rect.x <=0 or ball_rect.x >=800) or (ball_rect.y <=0 or ball_rect.y >=400):
        if ball_rect.y <= 0 and ball_vel_x <0 : #goes left-bottom #counter clock wise
            ball_vel_y = 4
            ball_vel_x = -4
        elif ball_rect.y <= 0 and ball_vel_x >0 : #goes right-bottom #clock wise
            ball_vel_y = 4
            ball_vel_x = 4
        
        if ball_rect.colliderect(player_rect1) and ball_vel_y >0: # goes bottom right #counter #clock wise
            ball_vel_y = 4
            ball_vel_x = 4
        elif ball_rect.colliderect(player_rect1) and ball_vel_y <0: # goes upper right #clock wise
            ball_vel_y = -4
            ball_vel_x = 4
            
        if ball_rect.y >=400 and ball_vel_x >0: #counter clock wise
            ball_vel_y = -4
            ball_vel_x = 4
        elif ball_rect.y >=400 and ball_vel_x <0: #clock wise
            ball_vel_y = -4
            ball_vel_x = -4
            
        if ball_rect.colliderect(player_rect2) and ball_vel_y >0: #counter clock wise
            ball_vel_y = 4
            ball_vel_x = -4
        elif ball_rect.colliderect(player_rect2) and ball_vel_y <0: #clock wise
            ball_vel_y = -4
            ball_vel_x = -4
        if ball_rect.x >= 850:
            score[0] = score[0] + 1
            game_active = False
            print(score)
        elif ball_rect.x <= -50:
            score[1] = score[1] + 1
            game_active = False
            print(score)
        
    
    key_pressed = pygame.key.get_pressed()
    p1_input(key_pressed,player_rect1)
    p2_input(key_pressed,player_rect2)
    pygame.display.update()
    clock.tick(60)