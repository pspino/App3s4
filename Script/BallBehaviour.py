import bpy
import math
import os

os.system("cls")

scene = bpy.context.scene
scene.frame_end = 1000

sphere = bpy.data.objects['Sphere']
sphere.select = True

sphere.rigid_body.kinematic = True

sphere.location = (0,0,10)
sphere.keyframe_insert(data_path="location", frame=1)

x = 0.5
y = 8.056
sphere.location = (0,x,y)
sphere.keyframe_insert(data_path="location", frame=4)

x = 1.25
y = 4.097
sphere.location = (0,x,y)
sphere.keyframe_insert(data_path="location", frame=20)

sphere.rigid_body.kinematic = False
