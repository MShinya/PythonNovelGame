import pygame
import SceneManager
import IScene
import GameSettings
import Game
import Load


class Menu(IScene.IScene):
    '''
    メニュー画面を担当するクラス
    メニュー画面にはタイトルとメニューが含まれる

    Inner Class
    -----------
    Menus : メニュー画面のメニュー項目に関する処理を担当するクラス

    Menber Functions
    ----------------
    __init__ : Menuクラスのコンストラクタ．背景画像の読み込みとMenusクラスのインスタンスを生成する．

    drawTitle : タイトルの描画を担当．

    draw : メニューとタイトルを実際に描画．

    eventProcess : イベント処理．
    '''

    # メニューのリスト
    # 中身はStringのタプルで，('実際に表示するテキスト' : 'クリックした時に遷移するシーン名')
    MenuText = [
        ('はじめから', 'Game'),
        ('つづきから', 'Load'),
        ('せってい', 'Game'),
        ('クレジット', 'Game'),
        ('やめる', 'Exit')
    ]

    class Menus():
        '''
        メニュー画面のメニューを担当するクラス
        '''
        def __init__(self, text: str, x: int, y: int, scene: str) -> None:
            '''
            Parameter
            ---------
            text : string
                メニューに表示する文字列
            x : int
                文字列の左上のx座標
            y : int
                文字列の左上のy座標
            scene : string
                押した時に切り替えるシーン
            '''
            self.textSurf = GameSettings.MenuFont.render(text, True, (0, 0, 0))
            self.mouseOverTextSurf = GameSettings.MenuFont.render(text, True, (200, 37, 50))
            self.mouseOverFlag = False
            self.text = text
            self.size = (self.textSurf.get_width(), self.textSurf.get_height())
            self.pos = (x, y)
            self.scene = scene

        def eventProcess(self) -> None:
            '''
            メニューがマウスオーバーされた時の動作
            '''
            if Menu.isMouseOver(self.pos[0], self.pos[1], self.size[0], self.size[1]):
                self.mouseOverFlag = True
                pygame.event.get()
                if pygame.mouse.get_pressed()[0]:
                    if self.scene == 'Game':
                        SceneManager.addScene('Game', Game.Game())
                    if self.scene == 'Load':
                        SceneManager.SceneList['Load'].Load()
                    Menu.cheangeScene(self.scene)
            else:
                self.mouseOverFlag = False

        def draw(self) -> None:
            '''
            メニューの描画
            '''
            if self.mouseOverFlag:
                Menu.screen.blit(self.mouseOverTextSurf, self.pos)
            else:
                Menu.screen.blit(self.textSurf, self.pos)

    def __init__(self) -> None:
        self.DrawList.append(pygame.image.load('images/background/sougen.jpg'))
        self.MenuList = []
        for i in range(len(self.MenuText)):
            self.MenuList.append(self.Menus(self.MenuText[i][0], 100, 300 + 80 * i, self.MenuText[i][1]))

    def drawTitle(self) -> None:
        '''
        ゲームのタイトルを作成、描画する関数
        '''
        title = GameSettings.TitleFont.render('ノベルゲームだよ', True, (0, 0, 0))
        self.screen.blit(title, (GameSettings.WindowSize[0] // 2 - title.get_width() // 2, 50))

    def draw(self) -> None:
        for img in self.DrawList:
            self.screen.blit(img, (0, 0))
        self.drawTitle()
        for M in self.MenuList:
            M.draw()

    def eventProcess(self) -> None:
        for M in self.MenuList:
            M.eventProcess()
