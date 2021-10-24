import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Interface")
font = pygame.font.SysFont('cambria.ttf', 30)

while True:
    screen.fill((255, 255, 255))
    screen.blit(font.render('Pratyus Mohapatra', True, (0, 0, 0)), (10, 10))
    screen.blit(font.render("Grade: 10", True, (0, 0, 0)), (10, 40))
    screen.blit(font.render("I absolutely loathe creating pygame windows.", True, (0, 0, 0)), (10, 70))
    pygame.display.update()
