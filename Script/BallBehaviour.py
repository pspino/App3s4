import bpy
import math
import os

os.system("cls")

#python scripted ball
scene = bpy.context.scene
scene.frame_end = 1000

sphere = bpy.data.objects['Sphere']
bpy.ops.rigidbody.objects_add(type='ACTIVE')
sphere.select = True

sphere.rigid_body.kinematic = True
sphere.keyframe_insert("rigid_body.kinematic",frame=1)

sphere.location = (0,0,10)
sphere.keyframe_insert(data_path="location", frame=1)
#0.1875	9.3359375
sphere.location = (0,0.1875,9.3359375)
sphere.keyframe_insert(data_path="location", frame=4)

sphere.rigid_body.kinematic=False
sphere.keyframe_insert("rigid_body.kinematic",frame=4)

#simulink ball
simulink = bpy.data.objects['Sphere.001']
simulink.select = True

frame_num = 0
rotx = 0
vitRotX = 0

path = os.path.dirname(os.path.dirname(__file__))
completePath = path + "/input.txt"
cpt=0
file = open(completePath, "r")
for line in file:
    cpt += 1
    print(cpt)
    y,z= line.strip(" \n[]").split("\t")
    location = 0, float(y), float(z)
    
    if frame_num == 24:
        vitRotX = 0.12
    if frame_num == 110:
        vitRotX = vitRotX + 0.12
    if frame_num == 178:
        vitRotX = vitRotX + 0.12
   
    if frame_num <= 227:
        rotx = rotx + vitRotX
    else:
        rotx = rotx + vitRotX/(frame_num*0.01)
    rotation = rotx, 0, 0
    
    bpy.context.scene.frame_set(frame_num)
    simulink.location = location
    simulink.keyframe_insert(data_path="location", index=-1)
    simulink.rotation_euler = rotation
    simulink.keyframe_insert(data_path="rotation_euler", index=-1)
    frame_num += 1

