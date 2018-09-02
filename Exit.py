import sys
import pygame
from pygame.locals import *
from IScene import *
import GameSettings

class Exit(IScene):
    '''
    メニュー画面を担当するクラス
    '''
    def __init__(self):
        self.flameImage = pygame.image.load('images/frame_wave_yoko.jpg')
        self.flamePos = ((GameSettings.WindowSize[0] - self.flameImage.get_size()[0]) // 2,
                         (GameSettings.WindowSize[1] - self.flameImage.get_size()[1]) // 2)
        self.questionText = GameSettings.QuestionFont.render('ゲームを終了しますか？', True, (0, 0, 0))
        self.questionPos = (self.flamePos[0] + (self.flameImage.get_size()[0] - self.questionText.get_size()[0]) // 2,
                            self.flamePos[1] + (self.flameImage.get_size()[1] - self.questionText.get_size()[1]) // 2)
        self.alternativeTexts = [GameSettings.AlternativeFont.render('はい', True, (0, 0, 0)),
                                 GameSettings.AlternativeFont.render('いいえ', True, (0, 0, 0))]
        self.alternativePos = [(self.flamePos[0] + (self.flameImage.get_size()[0] // 2 - self.alternativeTexts[0].get_size()[0]) // 2, 30),
                               (self.flamePos[0] + self.flameImage.get_size()[0] * 3 // 4 - self.alternativeTexts[1].get_size()[1] // 2, 30)]

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
