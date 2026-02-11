import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")
img = pygame.image.load("image.jpeg")
img = pygame.transform.scale(img, (300, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    win.fill((58, 58, 58))
    win.blit(img, (100, 100))
    
    pygame.display.flip()