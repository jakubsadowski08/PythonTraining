import pygame
import random
import linecache
from config import Config


def snake(
        x,
        y,
        body_x,
        body_y,
        gameDisplay,
        snakeIMG,
        bodyIMG,
):
    gameDisplay.blit(snakeIMG, (x, y))
    for i in range(len(body_x)):
        gameDisplay.blit(bodyIMG, (body_x[i], body_y[i]))


def apple(
        x,
        y,
        gameDisplay,
        appleIMG,
):
    gameDisplay.blit(appleIMG, (x, y))


def banana(
        x,
        y,
        gameDisplay,
        bananaIMG,
):
    gameDisplay.blit(bananaIMG, (x, y))


def checking(
        x,
        y,
        apple_x,
        apple_y,
):
    if x == apple_x and y == apple_y:
        return True
    else:
        return False


def end_of_game(
        x,
        y,
        body_x,
        body_y,
        display_width,
        display_height,
):
    if x >= display_width or x < 0 or y >= display_height or y < 0:
        return True
    else:
        for i in range(len(body_x)):
            if body_x[i] == x and body_y[i] == y:
                return True
        return False


def size_increasing(
        x,
        y,
        direction,
        directions,
        body_x,
        body_y,
):
    if direction == directions['Right']:
        body_x.append(x - 20)
        body_y.append(y)
    elif direction == directions['Left']:
        body_x.append(x + 20)
        body_y.append(y)
    elif direction == directions['Up']:
        body_x.append(x)
        body_y.append(y + 20)
    elif direction == directions['Down']:
        body_x.append(x)
        body_y.append(y - 20)


def events(direction, directions):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction \
                    != directions['Right']:
                direction = directions['Left']
            elif event.key == pygame.K_RIGHT and direction \
                    != directions['Left']:
                direction = directions['Right']
            elif event.key == pygame.K_UP and direction \
                    != directions['Down']:
                direction = directions['Up']
            elif event.key == pygame.K_DOWN and direction \
                    != directions['Up']:
                direction = directions['Down']

    return direction


def moving_snake(
        body_x,
        body_y,
        direction,
        directions,
        head_x,
        head_y,
):
    for i in reversed(range(len(body_x))):
        if i != 0:
            body_x[i] = body_x[i - 1]
            body_y[i] = body_y[i - 1]
        else:
            body_x[i] = head_x
            body_y[i] = head_y

    if direction == directions['Right']:
        head_x = head_x + 20
    elif direction == directions['Left']:
        head_x = head_x - 20
    elif direction == directions['Up']:
        head_y = head_y - 20
    elif direction == directions['Down']:
        head_y = head_y + 20
    return (head_x, head_y)


def default_values(head_x, head_y):
    return (Config.display_width * 0.5, Config.display_height * 0.5)


def cleanse_lists():
    Config.body_x = []
    Config.body_y = []


def main(gameDisplay):
    pygame.display.set_caption('snake')

    pygame.mixer.music.load('bg.wav')
    pygame.mixer.music.play(-1, 0.0)

    clock = pygame.time.Clock()

    score = 0

    font = pygame.font.SysFont('dejavusans', 20)
    text = 'Score: ' + str(score)
    text_render = font.render(text, 1, (0, 0, 0))

    snakeIMG = pygame.image.load('snake.png')
    appleIMG = pygame.image.load('apple.png')
    bodyIMG = pygame.image.load('body.png')
    bananaIMG = pygame.image.load('banana.png')
    bgIMG = pygame.image.load('background.png')

    round = 1

    speed_boost = False
    number_of_boosted_rounds = 0
    while not end_of_game(
            Config.head_x,
            Config.head_y,
            Config.body_x,
            Config.body_y,
            Config.display_width,
            Config.display_height,
    ):
        Config.direction = events(Config.direction, Config.directions)
        (Config.head_x, Config.head_y) = moving_snake(
            Config.body_x,
            Config.body_y,
            Config.direction,
            Config.directions,
            Config.head_x,
            Config.head_y,
        )
        gameDisplay.blit(bgIMG, (0, 0))
        gameDisplay.blit(text_render, (10, 10))
        if checking(Config.head_x, Config.head_y, Config.apple_x,
                    Config.apple_y):
            Config.apple_x = 20 * random.randint(0,
                                                 (Config.display_width - 20) / 20)
            Config.apple_y = 20 * random.randint(0,
                                                 (Config.display_height - 20) / 20)
            apple(Config.apple_x, Config.apple_y, gameDisplay, appleIMG)
            size_increasing(
                Config.head_x,
                Config.head_y,
                Config.direction,
                Config.directions,
                Config.body_x,
                Config.body_y,
            )
        else:
            apple(Config.apple_x, Config.apple_y, gameDisplay, appleIMG)
        if round >= 50 and speed_boost is False:
            banana(Config.banana_x, Config.banana_y, gameDisplay,
                   bananaIMG)
            if checking(Config.head_x, Config.head_y, Config.banana_x,
                        Config.banana_y):
                round = 1
                speed_boost = True
        snake(
            Config.head_x,
            Config.head_y,
            Config.body_x,
            Config.body_y,
            gameDisplay,
            snakeIMG,
            bodyIMG,
        )
        pygame.display.update()
        if speed_boost:
            if number_of_boosted_rounds < Config.boost_lenght:
                number_of_boosted_rounds = number_of_boosted_rounds + 1
                clock.tick(30)
            else:
                score = score + len(Config.body_x)
                text = 'Score: ' + str(score)
                text_render = font.render(text, 1, (0, 0, 0))
                number_of_boosted_rounds = 1
                speed_boost = False
        else:
            clock.tick(20)
        round = round + 1
    pygame.mixer.music.stop()
    (Config.head_x, Config.head_y) = default_values(Config.head_x,
                                                    Config.head_y)
    cleanse_lists()
    gameDisplay.fill(Config.black)
    gameover(gameDisplay,score)


def gameover(screen,score):
    linecache.clearcache()
    best_score = linecache.getline('best_score.txt', 1)
    if int(best_score) < score:
        file = open('best_score.txt', 'w')
        file.write(str(score))
        best_score = str(score) + '\n'
        file.close()
    pygame.display.set_caption('Game Over')

    font = pygame.font.SysFont('dejavusans', 40)
    text = 'Your score: ' + str(score)
    text_render = font.render(text, 1, (255, 255, 255))
    screen.blit(text_render, (280, 250))

    text = 'Best score: ' + best_score
    text_render = font.render(text[:-1], 1, (255, 255, 255))
    screen.blit(text_render, (280, 350))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(Config.black)
                intro(True, screen)


def intro(started, screen=pygame.display.set_mode((Config.display_width,
                                                   Config.display_height))):
    if not started:
        pygame.init()
    pygame.display.set_caption('Intro')
    startIMG = pygame.image.load('start.png').convert()
    stopIMG = pygame.image.load('stop.png').convert()

    screen.blit(startIMG, (Config.start_x, Config.start_y))
    screen.blit(stopIMG, (Config.stop_x, Config.stop_y))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                if x > Config.start_x and x < Config.start_x + 200 \
                        and y > Config.start_y and y < Config.start_y + 80:
                    main(screen)
                elif x > Config.stop_x and x < Config.start_x + 189 \
                        and y > Config.stop_y and y < Config.stop_y + 80:
                    pygame.quit()
                    quit()


intro(False)
