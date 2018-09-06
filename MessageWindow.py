import pygame
from pygame.locals import *
import GameSettings

class MessageWindow():
    lineImages = [None for _ in range(6)]
    lineNum = 0
    def __init__(self, message_window):
        self.dictMessageWindow =  message_window
        self.flameNumber = 0
        self.callOnceFlag = True
        self.callFlameOnceFlag = True

    def setChapter(self, chapter):
        self.dictMessageWindow = chapter
        self.flameNumber = 0
        self.callFlameOnceFlag = True

    def prepareLines(self):
        for i in range(len(self.dictMessageWindow['lines'])):
            if '<MainCharactorName>' in self.dictMessageWindow['lines'][i]:
                self.dictMessageWindow['lines'][i].replace('<MainCharactorName>', GameSettings.MainCharactorName)
        temp = [0 for _ in range(len(self.dictMessageWindow['lines']))]
        for i in range(len(self.dictMessageWindow['lines'])):
            temp[i] = [self.dictMessageWindow['lines'][i][28 * j:28 * (j + 1)] for j in range(len(self.dictMessageWindow['lines'][i]) // 28 + 1)]
        self.dictMessageWindow['lines'] = []
        for lines in temp:
            for line in lines:
                if line != '':
                    self.dictMessageWindow['lines'].append(line)
        self.lineNum = len(self.dictMessageWindow['lines'])
        self.callFlameOnceFlag = False

    def lineImage(self, screen):
        i = self.flameNumber // 28
        if i < self.lineNum:
            self.lineImages[i] = GameSettings.LinesFont.render(self.dictMessageWindow['lines'][i][:(self.flameNumber - 28 * i + 2)], True, (255, 255, 255))
        for j in range(self.lineNum):
            if self.lineImages[j] != None:
                screen.blit(self.lineImages[j], (self.textBoxPos[0] + 20, self.textBoxPos[1] + 50 + 25 * j))

    def callOnce(self):
        self.textBox = pygame.image.load('images/frame/textbox2.png').convert()
        self.textBox.set_colorkey((255, 0, 255))
        self.textBox.set_alpha(200)
        self.textBoxPos = ((GameSettings.WindowSize[0] - self.textBox.get_size()[0]) // 2,
                            GameSettings.WindowSize[1] - self.textBox.get_size()[1])
        self.callOnceFlag = False

    def update(self):
        self.flameNumber += 2
        if self.callOnceFlag:
            self.callOnce()
        if self.callFlameOnceFlag:
            self.prepareLines()
        if self.dictMessageWindow['name'] == 'MainCharactorName':
            self.dictMessageWindow['name'] = GameSettings.MainCharactorName

    def draw(self, screen):
        screen.blit(self.textBox, self.textBoxPos)
        self.lineImage(screen)
