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
        self.flameImage = pygame.image.load('images/frame/frame_wave_yoko.jpg')
        self.flamePos = ((GameSettings.WindowSize[0] - self.flameImage.get_size()[0]) // 2,
                         (GameSettings.WindowSize[1] - self.flameImage.get_size()[1]) // 2)
        self.questionText = GameSettings.QuestionFont.render('ゲームを終了しますか？', True, (0, 0, 0))
        self.questionPos = (self.flamePos[0] + (self.flameImage.get_size()[0] - self.questionText.get_size()[0]) // 2,
                            self.flamePos[1] + 80)
        self.alternativeTexts = [GameSettings.AlternativeFont.render('はい', True, (0, 0, 0)),
                                 GameSettings.AlternativeFont.render('いいえ', True, (0, 0, 0))]
        self.mouseOverAlternativeTexts = [GameSettings.AlternativeFont.render('はい', True, (255, 0, 0)),
                                          GameSettings.AlternativeFont.render('いいえ', True, (255, 0, 0))]
        self.alternativePos = [(self.flamePos[0] + (self.flameImage.get_size()[0] // 2 - self.alternativeTexts[0].get_size()[0]) // 2,\
                                self.flamePos[1] + self.flameImage.get_size()[1] - 80),
                               (self.flamePos[0] + self.flameImage.get_size()[0] * 3 // 4 - self.alternativeTexts[1].get_size()[1] // 2 - 40,\
                                self.flamePos[1] + self.flameImage.get_size()[1] - 80)]
        self.alternativeMouseOverFlag = [False, False]

    def update(self):
        #選択肢にマウスオーバーしているかを調べ処理します。
        for i in range(len(self.alternativeTexts)):
            x = self.alternativePos[i][0]
            y = self.alternativePos[i][1]
            width = self.alternativeTexts[i].get_size()[0]
            height = self.alternativeTexts[i].get_size()[1]
            if Exit.isMouseOver(x, y, width, height):
                self.alternativeMouseOverFlag[i] = True
                pygame.event.get()
                if pygame.mouse.get_pressed()[0]:
                    if i == 0:
                        pygame.quit()
                        sys.exit()
                    else:
                        Exit.cheangeScene(SceneManager.getBeforeScene().__class__.__name__)
            else:
                self.alternativeMouseOverFlag[i] = False

    def draw(self):
        SceneManager.getBeforeScene().draw()
        self.screen.blit(self.flameImage, self.flamePos)
        self.screen.blit(self.questionText, self.questionPos)
        for i in range(len(self.alternativeTexts)):
            if self.alternativeMouseOverFlag[i]:
                self.screen.blit(self.mouseOverAlternativeTexts[i], self.alternativePos[i])
            else:
                self.screen.blit(self.alternativeTexts[i], self.alternativePos[i])


                        



