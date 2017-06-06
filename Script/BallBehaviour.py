import bpy
import math
import os

os.system("cls")

scene = bpy.context.scene
scene.frame_end = 1000

sphere = bpy.data.objects['Sphere']
bpy.ops.rigidbody.objects_add(type='ACTIVE')
sphere.select = True

sphere.rigid_body.kinematic = True
sphere.keyframe_insert("rigid_body.kinematic",frame=1)

sphere.location = (0,0,10)
sphere.keyframe_insert(data_path="location", frame=1)

sphere.location = (0,0.25,9.097)
sphere.keyframe_insert(data_path="location", frame=4)

sphere.rigid_body.kinematic=False
sphere.keyframe_insert("rigid_body.kinematic",frame=4)
