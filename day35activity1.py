import pygame
import random

pygame.init()

SPRITECOLORCHANGE = pygame.USEREVENT + 1
BACKGROUNGCOLORCHANGE = pygame.USEREVENT + 2

blue = pygame.Color("blue")
lightblue = pygame.Color("lightblue")
darkblue = pygame.Color("darkblue")
yellow = pygame.Color("yellow")
magenta = pygame.Color("magenta")
orange = pygame.Color("orange")
white = pygame.Color("white")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    
    def update(self):
        self.rect.move_ip(self.velocity)
        hit = False
        if self.rect.left < 0 or self.rect.right > 500:
            self.velocity[0] = -self.velocity[0]
            hit = True
        if self.rect.top < 0 or self.rect.bottom > 400:
            self.velocity[1] = -self.velocity[1]
            hit = True
        if hit == True:
            pygame.event.post(pygame.event.Event(SPRITECOLORCHANGE))
            pygame.event.post(pygame.event.Event(BACKGROUNGCOLORCHANGE))
    
    def changeColor(self):
        self.image.fill(random.choice([yellow, magenta, orange, white]))

def changeBackgroundColor():
    global bgColor
    bgColor = random.choice([blue, lightblue, darkblue])

spriteList = pygame.sprite.Group()
sp1 = Sprite(white, 20, 20)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 380)
spriteList.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")
bgColor = blue
screen.fill(bgColor)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITECOLORCHANGE:
            sp1.changeColor()
        elif event.type == BACKGROUNGCOLORCHANGE:
            changeBackgroundColor()
    spriteList.update()
    screen.fill(bgColor)
    spriteList.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()