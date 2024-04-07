import pygame 
import random
pygame.init()

#to pause the game press 'Esc', to open settings menu press 's'

# unbreakable brick is a brick that needs to be hit 2 times to make it disappear
#bonus brick score x2

W, H = 1200, 650
FPS = 60

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 300 #150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1
color_index = 0
color_options = [{'color':'red', 'rgb':(255, 0, 0)}, {'color':'green', 'rgb':(0, 255, 0)}, {'color':'blue', 'rgb':(0, 0, 255)}]

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('sources/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (3)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 
# random number of unbreakable bricks 3-7
unbreakable_bricks_count = random.randrange(1, 7)
# random number of bonus bricks less or equal 6
bonus_bricks_count = random.randrange(1, 6)
# 0 - breakable, 1 - unbreakable, 2 - bonus
type_list = [1] * unbreakable_bricks_count + [2] * bonus_bricks_count + [0] * (len(block_list) - unbreakable_bricks_count - bonus_bricks_count)
random.shuffle(type_list)
#print(type_list)
# print(block_list)




#Menu
paused = False
settings_open = False

def pause_screen():
    global pausetext, pausetextRect
    global settings_button_text, settings_button_rect
    global paused, settings_open
    if not paused:
        paused = True
        screen.blit(pausetext, pausetextRect)  # Show pause text
    else:
        paused = False

def settings_menu():
    global settings_open, color_index
    settings_open = True
    while settings_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    color_index = (color_index - 1) % len(color_options)
                elif event.key == pygame.K_DOWN:
                    color_index = (color_index + 1) % len(color_options)
                elif event.key == pygame.K_RETURN:
                    settings_open = False

        screen.fill(bg)
        
        # Display "Settings" label
        settings_label_font = pygame.font.SysFont('comicsansms', 40)
        settings_label_text = settings_label_font.render('Settings Menu', True, (255, 255, 255))
        settings_label_rect = settings_label_text.get_rect()
        settings_label_rect.center = (W // 2, 50)
        screen.blit(settings_label_text, settings_label_rect)

        # Display color options
        settings_font = pygame.font.SysFont('comicsansms', 30)
        settings_text = settings_label_font.render('Color options:', True, (255, 255, 255))
        settings_rect = settings_text.get_rect()
        settings_rect.center = (W // 2, 120)
        screen.blit(settings_text, settings_rect)
        for i, color in enumerate(color_options):
            pygame.draw.circle(screen, color['rgb'], (W // 2, 200 + 50 * i), 20)
            if i == color_index:
                pygame.draw.circle(screen, (255, 255, 255), (W // 2, 200 + 50 * i), 25, 2)  # Highlight selected color

        # Display instructions
        instructions_font = pygame.font.SysFont('comicsansms', 30)
        instructions_text = instructions_font.render('Use UP/DOWN arrows to choose color. Press ENTER to apply.', True, (255, 255, 255))
        screen.blit(instructions_text, (W // 2 - instructions_text.get_width() // 2, H - 100))
        
        pygame.display.flip()
        clock.tick(FPS)


#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

#Pause Screen
pausefont = pygame.font.SysFont('comicsansms', 40)
pausetext = pausefont.render('Pause', True, (255, 255, 255))
pausetextRect = losetext.get_rect()
pausetextRect.center = (W // 2, H // 2)

#Adding an event to increase speed (every 3 seconds)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 3000)
#Adding an event to shred paddle (every 5 seconds)
SHRINK_PADDLE = pygame.USEREVENT + 2
pygame.time.set_timer(SHRINK_PADDLE, 5000)

while not done:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            ballSpeed += 0.5
            #print(ballSpeed)
        if event.type == SHRINK_PADDLE:
            paddleW -= 20
            paddle.width = paddleW  
            #print(paddleW)
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_screen()

            elif event.key == pygame.K_s:
                settings_menu()

    screen.fill(bg)
    
    if not paused:
        # print(next(enumerate(block_list)))
        [pygame.draw.rect(screen, color_list[color], block)
        for color, block in enumerate (block_list)] 
        
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(color_options[color_index]['rgb']), ball.center, ballRadius)
        # print(next(enumerate (block_list)))

        #Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        #Collision left 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        #Collision top
        if ball.centery < ballRadius + 50: 
            dy = -dy
        #Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        #Collision blocks
        hitIndex = ball.collidelist(block_list)

        if hitIndex != -1:
            if(type_list[hitIndex] == 0 or type_list[hitIndex] == 2):
                hitRect = block_list.pop(hitIndex)
                hitColor = color_list.pop(hitIndex)
                dx, dy = detect_collision(dx, dy, ball, hitRect)
                if(type_list[hitIndex] == 0):
                    game_score += 1
                elif(type_list[hitIndex] == 2):
                    if game_score > 0:
                        game_score = game_score * 2
                    else:
                        game_score += 5
            else:
                type_list[hitIndex] = 0
                hitRect = block_list[hitIndex]
                dx, dy = detect_collision(dx, dy, ball, hitRect)
            collision_sound.play()
            
        #Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
        
        #Win/lose screens
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
        elif not len(block_list):
            screen.fill((255,255, 255))
            screen.blit(wintext, wintextRect)

        #Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed

    else:
        screen.blit(pausetext, pausetextRect)
    pygame.display.flip()
    clock.tick(FPS)