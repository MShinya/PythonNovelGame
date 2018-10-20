import pygame
from pygame.locals import *
import GameSettings

class MessageWindow():
    def __init__(self, message_window):
        self.dictMessageWindow =  message_window
        self.flameNumber = 0
        self.callOnce()
        self.callChapterOnce()
        self.callOnceFlag = True
        self.callChapterOnceFlag = True

    def setChapter(self, chapter):
        self.dictMessageWindow = chapter
        self.flameNumber = 0
        self.callChapterOnceFlag = True

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

    def makeLineImage(self):
        self.lineImages = [[] for _ in range(6)]
        for i in range(len(self.dictMessageWindow['lines'])):
            line = self.dictMessageWindow['lines'][i]
            for j in range(len(line)):
                self.lineImages[i].append(GameSettings.LinesFont.render(line[:j + 1], True, (255, 255, 255)))

    def drawLines(self, screen):
        for i in range(self.flameNumber // 14 + 1):
            if i < len(self.lineImages) - 1:
                try:
                    screen.blit(self.lineImages[i][min((self.flameNumber - 13 * i) * 2, len(self.dictMessageWindow['lines'][i])) - 1], \
                                (self.textBoxPos[0] + 20, self.textBoxPos[1] + 50 + 25 * i))
                except:
                    pass

    def callOnce(self):
        self.textBox = pygame.image.load('images/frame/textbox2.png').convert()
        self.textBox.set_colorkey((255, 0, 255))
        self.textBox.set_alpha(200)
        self.textBoxPos = ((GameSettings.WindowSize[0] - self.textBox.get_size()[0]) // 2,
                            GameSettings.WindowSize[1] - self.textBox.get_size()[1])
        self.callOnceFlag = False

    def callChapterOnce(self):
        self.prepareLines()
        self.makeLineImage()
        if self.dictMessageWindow['name'] == 'MainCharactorName':
            self.dictMessageWindow['name'] = GameSettings.MainCharactorName
        self.textName = GameSettings.LinesFont.render(self.dictMessageWindow['name'], True, (255, 255, 255))
        self.callChapterOnceFlag = False

    def update(self):
        self.flameNumber += 1
        if self.callOnceFlag:
            self.callOnce()
        if self.callChapterOnceFlag:
            self.callChapterOnce()

    def draw(self, screen):
        screen.blit(self.textBox, self.textBoxPos)
        screen.blit(self.textName, (self.textBoxPos[0] + (196 - self.textName.get_size()[0]) // 2, self.textBoxPos[1] + 6))
        self.drawLines(screen)
