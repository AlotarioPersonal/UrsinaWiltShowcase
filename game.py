#main executable for (put the game name here when you come up with one)

#ursina imports, plus any external scripting
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from object_logic import testbutton, testingbrick, building

app = Ursina()

#sound import
#i am a god at naming conventions
foot = Audio('footstep')
head = Audio('hop')
wap = Audio('wap')
Entity.default_shader#get shader
Sky()#cool skybox wow
map = Entity(model='terrainBeta1.obj', texture='ggras',texture_scale=(400,400), scale=200, collider='mesh')
#(^)these both(v) are model imports
crowbar = Entity(model='crowbar', collider="mesh", parent=camera, texture="crowbar", position=(1, -0.56, 1.5), scale=0.02, rotation = (0, 90, 0))


global player #now everyone can modify player speed no matter what function you're in

player = FirstPersonController() #set the player character to the First Person controller prefab
#camera.clip_plane_far = 200
#scene.fog_density=0.001
#removed these because they fucked with texture rendering and also look like total and complete ass,
#re-enable clip_plane_far if you're experiencing serious lag

#modify player stats
player.jump_up_duration = 1.1
player.gravity = 0.4
player.speed == 7
player.cursor.color=color.black
player.height = 2

def input(key):
    if key == 'escape':
        quit()
        #if you remove this you won't be able to unlock your mouse or leave the program
    if key == 'space':
        head.play()
        #boing

testingbrick.initBrick()
#testingbrick.tester.position = player.position
#testbutton.initButton()
#both of these are debug, testbutton was literally just the same as testbrick
#don't believe me, re-enable and snap to player pos
building.initBuilding1()
print(player.position)

#this is the goober that follows you around
enemy = Entity(model="icosphere", collider='sphere', scale=1, texture='white_cube', position = (12, -478, 0))

#if you ever need a reason to physically revolt in public, here you go
def godDamnThisThingNeedsALotOfUselessFunctions():
    dmgEnemy -= 1

#makes goober man follow you and handles collisions with the funny Freeman weapon (crowbar)
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
            
#resets crowbar position to default
def crowbarReset():
    crowbar.rotation = (0, 90, 0)
    crowbar.position = (1, -0.56, 1.5)

#runs every frame, handles AI, sprinting, and the crowbar basically
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

#run this sucker
app.run()