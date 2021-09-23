import pygame
from random import randint

class Questao_6():

    def __init__(self):

        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption()
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.color = (0, 0, 0)
        self.position = (0, 0)
        self.finish = False

    def draw_square(self, surface, color, position):

        rect = pygame.Rect(position, (50, 50))
        pygame.draw.rect(surface, color, rect)

    def init_game(self):
        
        while not self.finish:
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            self.position = (randint(5, 395), randint(5, 395))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        self.draw_square(self.SCREEN, self.color, self.position)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.draw_square(self.SCREEN, self.color, self.position)

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_6().init_game()