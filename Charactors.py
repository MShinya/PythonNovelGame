import pygame
from pygame.locals import *
import GameSettings

class Charactors():
    def __init__(self, charactor):
        self.dictCharactor = charactor
        self.charactor_img = [None for _ in range(3)]
        self.charactor_pos = [None for _ in range(3)]
        self.charactor_alpha = [100 for _ in range(3)]

    def charactorImgLoad(self):
        if 'l_charactor' in self.dictCharactor['charactor_img']:
            if self.dictCharactor['charactor_img']['l_charactor']:
                self.charactor_img[0] = pygame.image.load(self.dictCharactor['charactor_img']['l_charactor']).convert()
                self.charactor_img[0].set_colorkey((255, 0, 255))
            else:
                self.charactor_img[0] = None
        if 'm_charactor' in self.dictCharactor['charactor_img']:
            if self.dictCharactor['charactor_img']['m_charactor']:
                self.charactor_img[1] = pygame.image.load(self.dictCharactor['charactor_img']['m_charactor']).convert()
                self.charactor_img[1].set_colorkey((255, 0, 255))
            else:
                self.charactor_img[1] = None
        if 'r_charactor' in self.dictCharactor['charactor_img']:
            if self.dictCharactor['charactor_img']['r_charactor']:
                self.charactor_img[2] = pygame.image.load(self.dictCharactor['charactor_img']['r_charactor']).convert()
                self.charactor_img[2].set_colorkey((255, 0, 255))
            else:
                self.charactor_img[2] = None

    def charactorSetPos(self):
        quadPos = [GameSettings.WindowSize[0] // 4 * i for i in range(1, 4)]
        quadCharaPos = [None for i in range(3)]
        for i in range(3):
            quadCharaPos[i] = quadPos[i] - self.charactor_img[i].get_size()[0] // 2 if self.charactor_img[i] else None
        self.charactor_pos = [(quadCharaPos[i], 100) for i in range(3)]
        

    def charactorImgDraw(self, screen):
        for i in range(3):
            if self.charactor_img[i]:
                self.charactor_img[i].set_alpha(self.charactor_alpha[i])
                screen.blit(self.charactor_img[i], self.charactor_pos[i])


    def update(self):
        self.charactorImgLoad()
        self.charactorSetPos()

    def draw(self, screen):
        self.charactorImgDraw(screen)
