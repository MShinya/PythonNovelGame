import json
import sys
import os
import pygame
import IScene
from Charactors import Charactors
from MessageWindow import MessageWindow


class Game(IScene.IScene):
    '''
    ゲーム本体を担当するクラス．行う仕事は
        1) スクリプトファイルの内容の解析
        2) 解析した内容に基づき，ゲーム画面の構築，音声の再生
        3) セーブ(ロードは暗号化のために別クラスにする)

    ゲームを最初から始めた時はコンストラクタのデフォルト引数を使って初期化し，
    ロードした時はLoadクラスによって初期化される．

    Menber Functions
    ----------------
    __init__ : Gameクラスを初期化するコンストラクタ．

    callChapterOnce : チャプターが一つ進むごとに一回だけ呼ばれる処理を書く．bgm，背景など

    setChapter : Gameクラスがもつチャプターの情報の更新を行う．

    update : 毎フレーム呼ばれ．ゲームの構成要素の更新を行う．

    draw : 毎フレーム呼ばれ．描画処理を行う．

    eventProcess : 毎フレーム呼ばれ，キー入力やマウス入力に応じた処理を行う．
    '''
    def __init__(self, scriptName: str = 'Script1.json', scriptStartChapterNumber: int = 1, sectionName: str = 'introduction', loadFlag: bool = False) -> None:
        '''
        ゲームの初期化を行う関数．
        ゲームが最初から始められた時は，デフォルト引数に基づいて初期化する．
        ロードされた時は，Loadクラスから渡された引数に基づき初期化する．

        Parameters
        ----------
        scriptName : String, default = 'Script1.json'
            スクリプトが書かれたjsonファイルを指定する．

        scriptStartLineNumber : int, default = 1
            スクリプトのどこから開始するかを指定する．デフォルトはチャプター１から．

        chapterName : String, default = ''
            チャプターの名前．
        '''
        with open('scripts/' + scriptName, 'r') as jsonScript:
            self.dictScript = json.load(jsonScript)
            '''
            スクリプトファイルを読み込み，ディクショナリーとして保存する．
            現在は一つのスクリプトファイルにしか対応していないが，複数のスクリプトファイルに対応する必要がある(18/10/14)

            スクリプトファイルの構造は以下の通り

            -----スクリプトファイル(scriptName)--------------------------
            |                                                           |
            |    ----セクション(sectionName)----------------------      |
            |    |                                               |      |
            |    |    ----チャプター(chapterName)------------    |      |
            |    |    |                                     |    |      |
            |    |    |                                     |    |      |
            |    |    ---------------------------------------    |      |
            |    |                                               |      |
            |    |    ----チャプター(chapterName)------------    |      |
            |    |    |                                     |    |      |
            |    |    |                                     |    |      |
            |    |    ---------------------------------------    |      |
            |    |                                               |      |
            |    |                       :                       |      |
            |    |                                               |      |
            |    -------------------------------------------------      |
            |                                                           |
            |    ----セクション(sectionName)----------------------      |
            |    |                                               |      |
            |    |    ----チャプター(chapterName)------------    |      |
            |    |    |                                     |    |      |
            |                                                           |
            |                            :                              |
            |                            :                              |
            |                            :                              |
            |                                                           |
            -------------------------------------------------------------
            *1 chapterName = sectionName + chapterNumber とし，chapterNumberは001から始まり，自動的にインクリメントされる
            *2 chapterNumberはセクションが変わるごとに初期化される(junp機能を実装する際に気をつける)
            '''

        self.scriptName = scriptName
        self.sectionName = sectionName
        self.chapterNumber = scriptStartChapterNumber
        self.chapterName = self.sectionName + str(self.chapterNumber).zfill(3)
        self.dictChapter = self.dictScript[self.sectionName][self.chapterName]
        self.Charactors = Charactors(self.dictChapter['charactor'])
        self.MessageWindow = MessageWindow(self.dictChapter['message_window'])
        self.saveDataDict = {'scriptName': self.scriptName,
                             'sectionName': self.sectionName,
                             'chapterNumber': self.chapterNumber,
                             'chapterName': self.chapterName,
                             'Charactors': self.Charactors,
                             'MessageWindow': self.MessageWindow,
                             }
        self.nextChapterFrag = True
        self.callChapterOnceFlag = True

    def callChapterOnce(self) -> None:
        '''
        チャプターで一度だけ実行すれば良い処理をこの関数で行う
        チャプターで呼ばれたかどうかの判定はcallChapterOnceFlagで管理する
        '''
        self.callChapterOnceFlag = False
        if "background_img" in self.dictChapter:
            self.background_img = pygame.image.load(self.dictChapter["background_img"])
            self.saveDataDict['background_img'] = self.dictChapter["background_img"]
        if "BGM" in self.dictChapter:
            self.BGM = pygame.mixer.music.load(self.dictChapter["BGM"])
            self.saveDataDict['BGM'] = self.dictChapter["BGM"]

    def setChapter(self) -> None:
        self.chapterNumber += 1
        self.chapterName = self.sectionName + str(self.chapterNumber).zfill(3)
        self.dictChapter = self.dictScript[self.sectionName][self.chapterName]
        self.Charactors.setChapter(self.dictChapter['charactor'])
        self.MessageWindow.setChapter(self.dictChapter['message_window'])
        self.saveDataDict = {'scriptName': self.scriptName,
                             'sectionName': self.sectionName,
                             'chapterNumber': self.chapterNumber,
                             'chapterName': self.chapterName,
                             'Charactors': self.Charactors,
                             'MessageWindow': self.MessageWindow,
                             }
        self.nextChapterFrag = False
        self.callChapterOnceFlag = True

    def update(self) -> None:
        if self.callChapterOnceFlag:
            self.callChapterOnce()
        self.Charactors.update()
        self.MessageWindow.update()

    def draw(self) -> None:
        self.screen.blit(self.background_img, (0, 0))
        self.Charactors.draw(self.screen)
        self.MessageWindow.draw(self.screen)

    def eventProcess(self) -> None:
        # マウスポインタが画面下部に移動したらメニューを表示
        if 290 <= pygame.mouse.get_pos()[0] <= 990 and 690 <= pygame.mouse.get_pos()[1] <= 720:
            Game.cheangeScene('GameUnderMenu')

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                # 終了処理
                pygame.quit()
                sys.exit()
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_RETURN:
                    # Enterキーが押された時
                    if self.nextChapterFrag:
                        self.setChapter()
            if event.type == pygame.locals.MOUSEBUTTONDOWN and event.button == 1:
                # マウスがクリックされた時
                if self.nextChapterFrag:
                    self.setChapter()
            if event.type == pygame.locals.KEYUP:
                self.nextChapterFrag = True
            if event.type == pygame.locals.MOUSEBUTTONUP:
                self.nextChapterFrag = True

    def Save(self) -> None:
        print('Game.Save() has been called')
        if not os.path.exists('savedata'):
            os.mkdir('savedata')
        with open('savedata/save.json', 'w') as savefile:
            json.dump(self.saveDataDict, savefile)

    def Load(self) -> None:
        pass
