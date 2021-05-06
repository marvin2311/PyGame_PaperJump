import pygame
import os
import sys
import random

BG_IMG = pygame.image.load(os.path.join("images", "background.png"))
HERO_IMG = pygame.image.load(os.path.join("images", "hero.png"))
PLAT_IMG = pygame.image.load(os.path.join("images", "platform2.png"))


class Plat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = HERO_IMG


WIN_WIDTH = 400
WIN_HEIGHT = 533

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Paper Climber!")

pygame.font.init()
SCORE_FONT = pygame.font.SysFont("comicsans", 30)

plates = [Plat(random.randrange(0, WIN_WIDTH-PLAT_IMG.get_size()[0]), random.randrange(0, WIN_HEIGHT)) for i in range(15)]


def main():
    x = 100
    y = 100
    dy = 0.0
    h = 200
    global score
    score = 0
    player = Player(x,y)
    first_game = True


    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        win.blit(BG_IMG, (0, 0))

        for plat in plates:
            win.blit(PLAT_IMG, (plat.x, plat.y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 4
            player.image = HERO_IMG
        if keys[pygame.K_RIGHT]:
            x += 4
            player.image = pygame.transform.flip(HERO_IMG, True, False)

        if y < h:
            y = h
            for plat in plates:
                plat.y = plat.y - dy
                if plat.y > WIN_HEIGHT:
                    plat.y = 0
                    plat.x = random.randrange(0, WIN_WIDTH-PLAT_IMG.get_size()[0])
                    score += 1


        dy += 0.2
        y += dy
        if y > WIN_HEIGHT:
            dy = -10

        for plat in plates:
            if (x + 50  > plat.x) and (x + 20 < plat.x + 68) and (y + 70 > plat.y) and (y + 70 < plat.y + 14) and dy > 0:
                dy = -10


        text = SCORE_FONT.render("Score: " + str(score), 1, (0, 0, 0))
        win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

        win.blit(player.image, (x, y))


        if x < 0-HERO_IMG.get_size()[0] or x > WIN_WIDTH or y > WIN_HEIGHT:
            menu(False)

        pygame.display.update()

def menu(first_game=True):
    menu_active = True

    while menu_active:
        win.blit(BG_IMG, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if first_game:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        else:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            points = font.render("Your Score: " + str(score), True, (0, 0, 0))
            scoreRect = points.get_rect()
            scoreRect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50)
            win.blit(points, scoreRect)
        textRect = text.get_rect()
        textRect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)
        win.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                main()

menu()
