import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Adding Sprites")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

sp1 = Player()
sp1.image.fill((255, 0, 0))
sp2 = Player()
sp2.image.fill((0, 0, 255))

sprites = pygame.sprite.Group()
sprites.add(sp1)
sprites.add(sp2)


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if sp1.rect.x < 0:
        sp1.rect.x = 0
    if sp1.rect.x > 450:
        sp1.rect.x = 450
    if sp1.rect.y < 0:
        sp1.rect.y = 0
    if sp1.rect.y > 450:
        sp1.rect.y = 450
    if keys[pygame.K_LEFT]:
        sp1.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        sp1.move(5, 0)
    if keys[pygame.K_UP]:
        sp1.move(0, -5)
    if keys[pygame.K_DOWN]:
        sp1.move(0, 5)

    win.fill((255, 255, 255))
    sprites.draw(win)
    pygame.display.flip()
    clock.tick(75)