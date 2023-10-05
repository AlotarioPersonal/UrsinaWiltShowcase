from ursina import *

def initBuilding1():
    global building1
    building1 = Entity(model="building.obj", collider='mesh',texture='brick', texture_scale=(3,3), scale=3)
    building1.x = 14
    building1.y = -472.9
    building1.z = -100
    building1.rotation_y=(-20)
    building1.rotation_z=(5)