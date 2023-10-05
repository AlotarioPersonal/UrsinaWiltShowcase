#main executable for (put the game name here when you come up with one)

#ursina imports, plus any external scripting
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from object_logic import testbutton, testingbrick, building
#start the app, initialize skybox, walls and floor
app = Ursina()

foot = Audio('footstep')
head = Audio('hop')
wap = Audio('wap')
Entity.default_shader
Sky()
map = Entity(model='terrainBeta1.obj', texture='ggras',texture_scale=(400,400), scale=200, collider='mesh')

crowbar = Entity(model='crowbar', collider="mesh", parent=camera, texture="crowbar", position=(1, -0.56, 1.5), scale=0.02, rotation = (0, 90, 0))


global player

player = FirstPersonController()
#camera.clip_plane_far = 200
#scene.fog_density=0.001


player.jump_up_duration = 1.1
player.gravity = 0.4
player.speed == 7
player.cursor.color=color.black
player.height = 2

def input(key):
    if key == 'escape':
        quit()
    if key == 'space':
        head.play()

testingbrick.initBrick()
#testingbrick.tester.position = player.position
#testbutton.initButton()
building.initBuilding1()
print(player.position)

enemy = Entity(model="icosphere", collider='sphere', scale=1, texture='white_cube', position = (12, -478, 0))
def godDamnThisThingNeedsALotOfUselessFunctions():
    dmgEnemy -= 1

def enemyAI():
    dister = 2
    if enemy.x != player.x:
        if enemy.x > player.x + dister:
            enemy.x -= 0.01
        else:
            enemy.x += 0.01
            
    if enemy.z != player.z:
        if enemy.z > player.z + dister:
            enemy.z -= 0.01
        else:
            enemy.z += 0.01
            
    if enemy.y != player.y:
        if enemy.y > player.y + dister:
            enemy.y -= 0.01
        else:
            enemy.y += 0.01
            
    if enemy.intersects(crowbar).hit:
        enemy.texture = ('greentest')
    else:
        enemy.texture = ('white_cube')
            

def crowbarReset():
    crowbar.rotation = (0, 90, 0)
    crowbar.position = (1, -0.56, 1.5)

def update():
    enemyAI()
    running = False
    crowbarStriking = False
    if held_keys['shift']:
        running = True
        player.speed = 15
        if foot.playing==True:
            print('silent second between steps')
        else:
            foot.play()
    if not held_keys['shift']: # check for button pressed while sprinting.
        running = False
        player.speed = 7
        
    if held_keys['left mouse']:
        #crowbarStriking == True
        crowbar.rotation = (15, 90, -45)
        crowbar.position = (-0.01, -0.56, 1.5)
        invoke(crowbarReset, delay=0.5)
        
app.run()