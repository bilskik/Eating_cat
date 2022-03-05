import pygame
import os.path

class snake():
    def __init__(self, window):
        self.window = window
    def main_loop(self):
        WIDTH, HEIGHT = 1100,750
        FPS = 60
        win = pygame.display.set_mode((WIDTH, HEIGHT))

        snake_image = pygame.image.load(os.path.join('kwadrat.png'))
        part_snake = pygame.transform.scale(snake_image, (50,50))

        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            win.blit(part_snake,(300, 100))
            pygame.display.update()

        pygame.quit()
        def draw(self):
            pass