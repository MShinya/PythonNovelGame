import json
import sys
import pygame
from pygame.locals import *
from IScene import *
from Charactors import Charactors
from MessageWindow import MessageWindow

class Game(IScene):
    '''
    メニュー画面を担当するクラス
    '''
    def __init__(self, scriptName = 'Script1.json', scriptStartLineNumber = 1, chapterName = ''):
        with open('scripts/' + scriptName, 'r') as jsonScript:
            self.dictScript = json.load(jsonScript)
        self.scriptName = scriptName
        self.chapterName = chapterName
        self.scriptLineNumber = scriptStartLineNumber
        self.chapterNumber = self.chapterName + str(scriptStartLineNumber).zfill(3)
        self.chapter = self.dictScript[self.chapterNumber]
        self.Charactors = Charactors(self.dictScript[self.chapterNumber]['charactor'])
        self.nextChapterFrag = True
        self.MessageWindow = MessageWindow(self.dictScript[self.chapterNumber]['message_window'])
        self.callChapterOnceFlag = True

    def callChapterOnce(self):
        self.callChapterOnceFlag = False
        if "background_img" in self.chapter:
            self.background_img = pygame.image.load(self.chapter["background_img"])
        if "BGM" in self.chapter:
            self.BGM = pygame.mixer.music.load(self.chapter["BGM"])

    def setChapter(self):
        self.scriptLineNumber += 1
        self.chapterNumber = self.chapterName + str(self.scriptLineNumber).zfill(3)
        self.Charactors.setChapter(self.dictScript[self.chapterNumber]['charactor'])
        self.MessageWindow.setChapter(self.dictScript[self.chapterNumber]['message_window'])
        self.nextChapterFrag = False
        self.chapter = self.dictScript[self.chapterNumber]
        self.callChapterOnceFlag = True

    def update(self):
        if self.callChapterOnceFlag:
            self.callChapterOnce()
        self.Charactors.update()
        self.MessageWindow.update()
        Game.eventCheck()

    def draw(self):
        self.screen.blit(self.background_img, (0, 0))
        self.Charactors.draw(self.screen)
        self.MessageWindow.draw(self.screen)

    def eventProcess(self):
        if 290 <= pygame.mouse.get_pos()[0] <= 990 and 690 <= pygame.mouse.get_pos()[1] <= 720:
            Game.cheangeScene('GameUnderMenu')
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if self.nextChapterFrag:
                        self.setChapter()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.nextChapterFrag:
                    self.scriptLineNumber += 1
                    self.chapterNumber = self.chapterName + str(self.scriptLineNumber).zfill(3)
                    self.Charactors.setChapter(self.dictScript[self.chapterNumber]['charactor'])
                    self.MessageWindow.setChapter(self.dictScript[self.chapterNumber]['message_window'])
                    self.nextChapterFrag = False
            if event.type == KEYUP:
                self.nextChapterFrag = True
            if event.type == MOUSEBUTTONUP:
                self.nextChapterFrag = True


    @classmethod
    def eventCheck(cls):
        pass

    def Save(self):
        pass

    def Load(self):
        pass
