import pygame
import random

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Space Invader 1")
enx = random.randint(50, 450)
eny = random.randint(50, 100)
font = pygame.font.SysFont("consolas", 30)
pygame.mixer.music.load("bgSoundForSI2.mp3")
pygame.mixer.music.play(-1)
score = 0
text = font.render(f"Score: {score}", True, (255, 255, 255))
msg = font.render("Congratulations!", True, (255, 0, 0))
colours = [(255, 100, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
background = pygame.image.load("image.jpeg")
background = pygame.transform.scale(background, (500, 500))


class Sprite(pygame.sprite.Sprite):
    def __init__(self, a, b, colour):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.center = (a, b)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


player = Sprite(250, 450, (255, 0, 0))
bullet = Sprite(-50, -50, (150, 150, 150))
bullet.image = pygame.Surface((10, 10))
enemy1 = Sprite(random.randint(50, 450), random.randint(50, 100), random.choice(colours))
enemy2 = Sprite(random.randint(50, 450), random.randint(50, 100), random.choice(colours))
enemy3 = Sprite(random.randint(50, 450), random.randint(50, 100), random.choice(colours))
enemy4 = Sprite(random.randint(50, 450), random.randint(50, 100), random.choice(colours))
enemy5 = Sprite(random.randint(50, 450), random.randint(50, 100), random.choice(colours))
enemy6 = Sprite(random.randint(50, 450), random.randint(50, 100), random.choice(colours))
enemy7 = Sprite(random.randint(50, 450), random.randint(50, 100), random.choice(colours))

sprites = pygame.sprite.Group()
sprites.add(player)
sprites.add(bullet)
sprites.add(enemy1)
sprites.add(enemy2)
sprites.add(enemy3)
sprites.add(enemy4)
sprites.add(enemy5)
sprites.add(enemy6)
sprites.add(enemy7)

running = True
shoot = False
clock = pygame.time.Clock()
while running:
    if shoot == False:
        bullet.rect.x = player.rect.x + 20
        bullet.rect.y = player.rect.y - 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_UP]:
        player.move(0, -5)
    if keys[pygame.K_DOWN]:
        player.move(0, 5)
    if keys[pygame.K_SPACE] and shoot == False:
        shoot = True
    if shoot == True:
        bullet.move(0, -10)
    if bullet.rect.y < 0:
        shoot = False
    if pygame.sprite.collide_rect(bullet, enemy1):
        shoot = False
        enemy1.rect.x = 10000
        enemy1.rect.y = 10000
        score += 1
    if pygame.sprite.collide_rect(bullet, enemy2):
        shoot = False
        enemy2.rect.x = 10000
        enemy2.rect.y = 10000
        score += 1
    if pygame.sprite.collide_rect(bullet, enemy3):
        shoot = False
        enemy3.rect.x = 10000
        enemy3.rect.y = 10000
        score += 1
    if pygame.sprite.collide_rect(bullet, enemy4):
        shoot = False
        enemy4.rect.x = 10000
        enemy4.rect.y = 10000
        score += 1
    if pygame.sprite.collide_rect(bullet, enemy5):
        shoot = False
        enemy5.rect.x = 10000
        enemy5.rect.y = 10000
        score += 1
    if pygame.sprite.collide_rect(bullet, enemy6):
        shoot = False
        enemy6.rect.x = 10000
        enemy6.rect.y = 10000
        score += 1
    if pygame.sprite.collide_rect(bullet, enemy7):
        shoot = False
        enemy7.rect.x = 10000
        enemy7.rect.y = 10000
        score += 1

    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.x > 450:
        player.rect.x = 450
    if player.rect.y < 0:
        player.rect.y = 0
    if player.rect.y > 450:
        player.rect.y = 450

    if pygame.sprite.collide_rect(player, enemy1):
        score += 1
    if pygame.sprite.collide_rect(player, enemy2):
        score += 1
    if pygame.sprite.collide_rect(player, enemy3):
        score += 1
    if pygame.sprite.collide_rect(player, enemy4):
        score += 1
    if pygame.sprite.collide_rect(player, enemy5):
        score += 1
    if pygame.sprite.collide_rect(player, enemy6):
        score += 1
    if pygame.sprite.collide_rect(player, enemy7):
        score += 1

    win.fill((255, 255, 255))
    win.blit(background, (0, 0))
    sprites.draw(win)
    win.blit(text, (10, 10))
    if score == 7:
        win.blit(msg, (100, 200))
    pygame.display.flip()
    clock.tick(75)
