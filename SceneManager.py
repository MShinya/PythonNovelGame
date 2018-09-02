import Menu
import Game
import Exit

SceneList = {'Menu': Menu.Menu(), 'Game': Game.Game(), 'Exit': Exit.Exit()}
BeforeScene = SceneList['Menu']
CurrentScene = SceneList['Menu']   

def getScene():
    '''
    現在いるシーンのインスタンスを返します。
    '''
    return CurrentScene

def getBeforeScene():
    '''
    一つ前のシーンのインスタンスを返します。
    '''
    return BeforeScene

def setScene(scene):
    '''
    シーン名を受け取り、現在のシーンを切り替えます。
    '''
    global BeforeScene
    global CurrentScene
    global SceneList
    BeforeScene = CurrentScene
    CurrentScene = SceneList[scene]
#class SceneManager():
#    '''
#    シーンの管理を行うクラス
#
#    Attributes
#    ----------
#    __BeforeScene : class
#        一つ前のクラスを記憶します
#    __CurrentScene : class
#        現在のクラスを記憶します
#    __SceneList : dict
#        すべてのシーンクラスのインスタンスを保持しています。シーン名で要素にアクセスできます。
#    '''
#
#    __SceneList = {'Menu': Menu.Menu(), 'Game': Game.Game()}
#    __BeforeScene = __SceneList['Menu']
#    __CurrentScene = __SceneList['Menu']   
#
#    @property
#    def Scene(self):
#        '''
#        現在どのシーンかを返します
#        '''
#        return self.__CurrentScene
#
#    @Scene.setter
#    def Scene(self, scene):
#        '''
#        シーンの切り替えを行う関数です。__BeforeSceneに一つ前のシーンを記憶します
#        
#        Parameters
#        ----------
#        scene : string
#            切り替えたいシーン名を文字列で受け取ります。
#        '''
#        self.__BeforeScene = self.__CurrentScene
#        self.__CurrentScene = self.__SceneList[scene]
