import pygame

size = width, height = 1920, 1080


def lobbi(screen):
    clock = pygame.time.Clock()
    background_image = pygame.image.load('background.png') #каринку закинуть в папку и проектом

    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(80)


if __name__ == "__main__":
    pygame.init()

    size = width, height
    screen = pygame.display.set_mode(size)

    lobbi(screen)
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
