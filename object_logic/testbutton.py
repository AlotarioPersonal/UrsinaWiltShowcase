from ursina import *

currentstring = "Click the box to move it over a slight amount"

def popUpText():
    global popup_text
    popup_text = Text(currentstring)
    
    
def destroyText():
    destroy(popup_text)
    
def moveButton():
    tester.x += 0.5
    
def initButton():
    global tester
    tester = Entity(model='testbutton.obj', scale_y=1, collider='mesh', texture='greentest.png', on_mouse_enter=popUpText, on_mouse_exit=destroyText, on_click=moveButton)
    tester.x += 5