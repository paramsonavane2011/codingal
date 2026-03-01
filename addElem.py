import pygame

pygame.init()

win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Game Screen")
win.fill((255, 255, 255))
font = pygame.font.SysFont("Arial", 30)
text = font.render("Hello, World!", True, (0, 0, 0))
rect = pygame.Rect(640 / 2 - 100, 480 / 2 - 50, 200, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), rect)
    win.blit(text, (640 / 2 - 100, 480 / 2 - 50))

    pygame.display.flip()