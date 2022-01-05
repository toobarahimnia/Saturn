from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random as ra
import numpy as np
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

window.color = color.black  # color.rgb(0,0,0)


def input(key):
    if key == 'escape' or key == 'q':
        quit()
    if key == 'up arrow':
        saturn.scale *= 1.5
        ring.scale *= 1.5
    if key == 'down arrow':
        saturn.scale /= 1.5
        ring.scale /= 1.5

fixed_entity = Entity(model='sphere', texture='assets/saturn', scale=500)


def update():
    fixed_entity.rotation_z += 0.5 * np.cos(60)
    saturn.rotation_x = 80
    saturn.reparent_to(fixed_entity)

    # color/ background?
    # for x in range(5):
    #     for z in range(5):  # adjusts the speed of rotation
                # Entity(model='plane', scale=fixed_entity.scale, color=color.gray, shader=lit_with_shadows_shader)  #scale fixed the pixel
                # Entity(model='cube', y=1, shader=lit_with_shadows_shader)
                # pivot = Entity
                # DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(20, -20, 20))


saturn = Entity(model='sphere', texture='assets/saturn', scale=3000)
cam_lens = 227.9 * 2 + 1000

# Saturn Ring
saturn.rings = True  # Saturn ;)
ring = Entity(model='cube', scale=saturn.scale*2.5, texture='assets/saturn_ring')
ring.position = saturn.position
ring.rotation_x = 80
ring.scale_y = 4
ring.reparent_to(fixed_entity)

project = FirstPersonController()
smithy = EditorCamera(move_speed=9000, parent=cam_lens)
# camera.clip_plane_far = 2e10



smithy.y = 8000
smithy.rotation_x = 90

jessie = Sky()
jessie.texture = 'assets/space_texture'

app.run()
