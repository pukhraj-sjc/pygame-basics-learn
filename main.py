# !/usr/bin/python
"""
Owner: Pukhraj
Description :- learning concepts of pygame
module install command:- pip install pygame==2.0.0.dev4
"""
# Standard Modules
import pygame
from bullet import projectile
from enemy import kilvish

pygame.init()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Pukhraj")
walkRight = [pygame.image.load('./gallery/sprites/R1.png'), pygame.image.load('./gallery/sprites/R2.png'), pygame.image.load('./gallery/sprites/R3.png'), pygame.image.load('./gallery/sprites/R4.png'), pygame.image.load('./gallery/sprites/R5.png'), pygame.image.load('./gallery/sprites/R6.png'), pygame.image.load('./gallery/sprites/R7.png'), pygame.image.load('./gallery/sprites/R8.png'), pygame.image.load('./gallery/sprites/R9.png')]
walkLeft = [pygame.image.load('./gallery/sprites/L1.png'), pygame.image.load('./gallery/sprites/L2.png'), pygame.image.load('./gallery/sprites/L3.png'), pygame.image.load('./gallery/sprites/L4.png'), pygame.image.load('./gallery/sprites/L5.png'), pygame.image.load('./gallery/sprites/L6.png'), pygame.image.load('./gallery/sprites/L7.png'), pygame.image.load('./gallery/sprites/L8.png'), pygame.image.load('./gallery/sprites/L9.png')]
bg = pygame.image.load('./gallery/sprites/bg.jpg')
char = pygame.image.load('./gallery/sprites/standing.png')
score = 0

class player(object):
    """
    This class creates the player
    """
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.walkCount = 0
        self.standing = True
        self.left = False
        self.right = False
        self.hitbox = (self.x + 17, self.y + 11, 25, 52)

    def draw(self,win):
        """
        function used to blit the player on user interface
        :param win:
        :return:
        """
        if self.walkCount +1 >= 27:
            self.walkCount = 0

        if self.right:
            win.blit(walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        elif self.left:
            win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char,(self.x,self.y))
        self.hitbox = (self.x + 17, self.y + 11, 25, 52)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


def redrawGameWindow():
    """
    common function to call all the draw functions of each class
    :return:
    """
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (390, 10))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    goblin.draw(win)



if __name__ == "__main__":
    font = pygame.font.SysFont("comicsans", 30, True)
    man = player(0,410,64,64)
    bullets = []
    running = True
    goblin = kilvish(0, 410, 64, 64, 450)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for bullet in bullets:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[2]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            man.x -= man.vel
            man.right = False
            man.left = True
        elif keys[pygame.K_RIGHT]:
            man.x += man.vel
            man.right = True
            man.left = False
        else:
            man.standing = True
            man.walkCount = 0

        if keys[pygame.K_SPACE]:
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bullets.append(projectile(round(man.x + man.width//2),round(man.y + man.height//2),6,(0,0,0),facing))

        redrawGameWindow()
        pygame.display.update()
pygame.quit()
