import pygame,random
from config import Config
def snake(x,y,body_x,body_y,gameDisplay,snakeIMG,bodyIMG):
    gameDisplay.blit(snakeIMG, (x,y))
    for i in range(len(body_x)):
        gameDisplay.blit(bodyIMG, (body_x[i],body_y[i]))
def apple(x,y,gameDisplay,appleIMG):
    gameDisplay.blit(appleIMG, (x,y))
def checking(x,y,apple_x,apple_y):
    if x == apple_x and y == apple_y:
        return True
    else:
        return False
def end_of_game(x,y,body_x,body_y,display_width,display_height):
    if x >= display_width or x < 0 or y >= display_height or y < 0:
        print(x,y)
        return True
    else:
        for i in range(len(body_x)):
            if body_x[i] == x and body_y[i] ==y:
                return True
        return False
def size_increasing(x,y,direction,directions,body_x,body_y):
    if direction == directions["Right"]:
        body_x.append(x-20)
        body_y.append(y)
    elif direction == directions["Left"]:
        body_x.append(x+20)
        body_y.append(y)
    elif direction == directions["Up"]:
        body_x.append(x)
        body_y.append(y+20)
    elif direction == directions["Down"]:
        body_x.append(x)
        body_y.append(y-20)
def events(direction, directions):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != directions["Right"]:
                direction = directions["Left"]
            elif event.key == pygame.K_RIGHT and direction != directions["Left"]:
                direction = directions["Right"] 
            elif event.key == pygame.K_UP and direction != directions["Down"]:
                direction = directions["Up"] 
            elif event.key == pygame.K_DOWN and direction != directions["Up"]:
                direction = directions["Down"]
    return direction

def moving_snake(body_x, body_y, direction, directions, head_x, head_y):
    for i in reversed(range(len(body_x))):
        if i !=0:
            body_x[i] =body_x[i-1]
            body_y[i] =body_y[i-1]
        else:
            body_x[i] =head_x
            body_y[i] =head_y
    
    if direction == directions["Right"]:
        head_x=head_x+20
    elif direction == directions["Left"]:
        head_x=head_x-20
    elif direction == directions["Up"]:
        head_y=head_y-20
    elif direction == directions["Down"]:
        head_y=head_y+20
    return head_x, head_y

def main(head_x,head_y,apple_x,apple_y,white,display_width,display_height,body_x,body_y,direction,directions):
    pygame.init()
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    bg = pygame.mixer.Sound('bg.wav')
    bg.play()
    snakeIMG = pygame.image.load('snake.png')
    appleIMG = pygame.image.load('apple.png')
    bodyIMG = pygame.image.load('body.png')
    while not end_of_game(head_x,head_y,body_x,body_y,Config.display_width,Config.display_height):
        direction = events(direction, directions)
        head_x, head_y = moving_snake(body_x, body_y, direction, directions, head_x, head_y)
        gameDisplay.fill(white)
        if  checking(head_x,head_y,apple_x,apple_y):
            apple_x =20 * random.randint(0,39)
            apple_y =20 * random.randint(0,29)
            apple(apple_x,apple_y,gameDisplay,appleIMG)
            size_increasing(head_x,head_y,direction,directions,body_x,body_y)
        else:
            apple(apple_x,apple_y,gameDisplay,appleIMG)
        snake(head_x,head_y,body_x,body_y,gameDisplay,snakeIMG,bodyIMG)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
main(Config.head_x,Config.head_y,Config.apple_x,Config.apple_y,Config.white,Config.display_width,Config.display_height,Config.body_x,Config.body_y,Config.direction,Config.directions)