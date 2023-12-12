import pygame

size = width, height = 1920, 1080


def lobbi(screen, running):
    clock = pygame.time.Clock()
    background_image = pygame.image.load('background.png')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, (75, 0, 130), (20, 400, 350, 125))
        pygame.draw.rect(screen, (75, 0, 130), (20, 550, 300, 125))

        game_name_text = pygame.font.SysFont('serif', 200).render("Гонки", False, (255, 105, 180))
        screen.blit(game_name_text, (10, 100))

        play_text = pygame.font.SysFont('serif', 100).render("Играть", False, (60, 60, 190))
        screen.blit(play_text, (50, 400))

        exit_text = pygame.font.SysFont('serif', 100).render("Выход", False, (60, 60, 190))
        screen.blit(exit_text, (35, 550))

        pygame.display.update()
        clock.tick(80)


if __name__ == "__main__":
    pygame.init()

    size = width, height
    running = True
    screen = pygame.display.set_mode(size)

    lobbi(screen, running)
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
