import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
app=Ursina()
Hb1=HealthBar(bar_color=color.blue)
ground=Entity(
    model='plane',
    texture='grass',
    collider='mesh',
    scale=(100,1,100)
)
player=FirstPersonController()
app.run()
