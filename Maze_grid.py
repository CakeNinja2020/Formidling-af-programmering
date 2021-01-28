import sys
import pygame
from pygame.locals import KEYDOWN, K_q

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 600, 400
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
YELLOW = (225,255,0)
PINK = (255,204,255)

# VARS:
_VARS = {'surf': False}


def main():
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    _VARS['surf'].fill(GREY)
    drawGrid(6)
    drawObs()
    drawCheese()
    while True:
        checkEvents()
        drawMouse()
        pygame.display.update()


n = 11452324253343
ID = ([int(d) for d in str(n)])
IDobs = ([int(d) for d in str(n)])


# Draw filled rectangle at coordinates x,y 18,18 with size width,height
# 60,60
def drawObs():

    for x in range(0, 4):
        IDobs.pop(0)
    print(IDobs)

    for i in range(0, (int(len(IDobs))), 2):
        x = IDobs[i]
        y = IDobs[i + 1]
        print(x, y)
        pygame.draw.rect(
            _VARS['surf'], BLACK,
            (15 + (x - 1) * 50, 15 + (y - 1) * 50, 42, 42))


        # pygame.draw


def drawMouse():
    #print(n)
    x = (ID[0])
    y = (ID[1])
    pygame.draw.rect(
        _VARS['surf'], PINK,
        (15 + (x - 1) * 50, 15 + (y - 1) * 50, 42, 42))


def drawCheese():
    x = (ID[2])
    y = (ID[3])
    pygame.draw.rect(
        _VARS['surf'], YELLOW,
        (15 + (x - 1) * 50, 15 + (y - 1) * 50, 42, 42))


def drawGrid(divisions):
    CONTAINER_WIDTH_HEIGHT = 300  # Not to be confused with SCREENSIZE
    cont_x, cont_y = 10, 10  # TOP LEFT OF CONTAINER

    # DRAW Grid Border:
    # TOP lEFT TO RIGHT
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (cont_x, cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y), 2)
    # # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (cont_x, CONTAINER_WIDTH_HEIGHT + cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x, CONTAINER_WIDTH_HEIGHT + cont_y), 2)
    # # LEFT TOP TO BOTTOM
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (cont_x, cont_y),
        (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT), 2)
    # # RIGHT TOP TO BOTTOM
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x, CONTAINER_WIDTH_HEIGHT + cont_y), 2)

    # Get cell size, just one since its a square grid.
    cellSize = CONTAINER_WIDTH_HEIGHT / divisions

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(divisions):
        pygame.draw.line(
            _VARS['surf'], BLACK,
            (cont_x + (cellSize * x), cont_y),
            (cont_x + (cellSize * x), CONTAINER_WIDTH_HEIGHT + cont_y), 2)
        # # HORIZONTAl DIVISIONS
        pygame.draw.line(
            _VARS['surf'], BLACK,
            (cont_x, cont_y + (cellSize * x)),
            (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y + (cellSize * x)), 2)


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()
