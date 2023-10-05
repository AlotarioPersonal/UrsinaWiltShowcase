from ursina import *

hasCoolBrick = False

def popUpText():
    global popup_text
    popup_text = Text("(Left Click) Collect Brick of Stock Pixelated TV Static")
    popup_text.y += 0.05
    popup_text.x -= 0.02
    
    
def destroyText():
    destroy(popup_text)
    
def moveBox():
    destroy(tester)
    destroyText()
    hasCoolBrick == True
    yay = Audio('getstatic')
    yay.play()
    
    
def initBrick():
    global tester
    tester = Entity(model='cube', scale_y=2, collider='box', texture='piss.jpg', on_mouse_enter=popUpText, on_mouse_exit=destroyText, on_click=moveBox)
    tester.x = 14
    tester.y = -471.7
    tester.z = -100
    tester.rotation_y=(-20)
    tester.rotation_z=(5)