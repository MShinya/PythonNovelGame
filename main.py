import sys
import pygame
from pygame.locals import *
import GameSettings
import SceneManager
import IScene

def main():
    pygame.init()
    screen = pygame.display.set_mode(GameSettings.WindowSize)
    pygame.display.set_caption(GameSettings.GameTitle)
    pygame.key.set_repeat(1)
    clock = pygame.time.Clock()
    IScene.IScene.setScreen(screen)
    
    while True:
        '''
        メインループ
        '''
        screen.fill((0, 0, 0))

        SceneManager.getScene().update()

        SceneManager.getScene().draw()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(GameSettings.FrameRate)

if __name__ == '__main__':
    main()
