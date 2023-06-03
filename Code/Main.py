import pygame, sys
from Settings import *
from Level import Level
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame .display.set_caption("Brodilochka")
        pygame_icon = pygame.image.load("../Graphics/Test/Player.png")
        pygame.display.set_icon(pygame_icon)
        self.clock = pygame.time.Clock()

        self.level = Level()

        main_sound = pygame.mixer.Sound("../Audio/Main.ogg")
        main_sound.set_volume(0.1)
        main_sound.play(loops = -1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
            
            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
