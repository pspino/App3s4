import bpy
import math
import os

os.system("cls")

scene = bpy.context.scene
scene.frame_end = 1000

sphere = bpy.data.objects['Sphere']
sphere.select = True

sphere.location.x = 0
sphere.location.y = 0
sphere.location.z = 10
x = sphere.location.x
y = sphere.location.z
g = -5
vy = -5
vx = 1.5

rayon = 1.5
sol = 1.2

for frameNum in range(scene.frame_end + 1):
    scene.frame_set(frameNum)
    x = vx*(frameNum/24) 
    y = (g/2)*(x/vx)**2 + vy*(x/vx) + 10
    sphere.location = (0,x,y)
    sphere.keyframe_insert(data_path="location", index=-1)
    print((x,y))
