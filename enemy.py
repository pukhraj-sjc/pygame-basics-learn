import pygame

class kilvish(object):
    walkRight = [pygame.image.load('./gallery/sprites/R1E.png'), pygame.image.load('./gallery/sprites/R2E.png'),
                 pygame.image.load('./gallery/sprites/R3E.png'), pygame.image.load('./gallery/sprites/R4E.png'),
                 pygame.image.load('./gallery/sprites/R5E.png'), pygame.image.load('./gallery/sprites/R6E.png'),
                 pygame.image.load('./gallery/sprites/R7E.png'), pygame.image.load('./gallery/sprites/R8E.png'),
                 pygame.image.load('./gallery/sprites/R9E.png'), pygame.image.load('./gallery/sprites/R10E.png'),
                 pygame.image.load('./gallery/sprites/R11E.png')]
    walkLeft = [pygame.image.load('./gallery/sprites/L1E.png'), pygame.image.load('./gallery/sprites/L2E.png'),
                pygame.image.load('./gallery/sprites/L3E.png'), pygame.image.load('./gallery/sprites/L4E.png'),
                pygame.image.load('./gallery/sprites/L5E.png'), pygame.image.load('./gallery/sprites/L6E.png'),
                pygame.image.load('./gallery/sprites/L7E.png'), pygame.image.load('./gallery/sprites/L8E.png'),
                pygame.image.load('./gallery/sprites/L9E.png'), pygame.image.load('./gallery/sprites/L10E.png'),
                pygame.image.load('./gallery/sprites/L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x,self.end]
        self.walkCount = 0
        self.health = 10
        self.vel = 3
        self.hitbox = (self.x + 17,self.y+2, 31,57)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def draw(self,win):
        self.move()
        if self.walkCount +1 >= 33:
            self.walkCount = 0

        if self.vel>0:
            win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1

        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
       # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        #pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            print('hit')
if __name__ == "__main__":
    pass
