import Menu
# import Game
import Exit
import Save
import GameUnderMenu

# SceneList から 'Game': Game.Game() を削除してある
# 後からMenuクラスによって追加される．
SceneList = {'Menu': Menu.Menu(), 'GameUnderMenu': GameUnderMenu.GameUnderMenu(), 'Exit': Exit.Exit(), 'Save': Save.Save()}
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


def addScene(newSceneName, newSceneObject):
    '''
    新しいシーンを追加します
    '''
    SceneList[newSceneName] = newSceneObject
