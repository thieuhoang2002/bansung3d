from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):
    def __init__(self, position=(0, 2, 0), color=color.red, health=100):
        # super().__init__(
        #     model='assets/models/animation/cutegirl/stand.gltf',
        #     color=color,
        #     position=position,
        #     speed=80,
        #     jump_height=3,
        #     gravity=1.5,
        #     origin_y=-.5,  # Đặt tâm mô hình ở đáy
        #     collider='box',
        #     z=-10
        # )
        super().__init__(model='cube', z=-10, color=color, origin_y=-.5, speed=16, collider='box')
        self.collider = BoxCollider(self, Vec3(0,1,0), Vec3(1,2,1))
        self.health = health
        self.gun = None
        # Tùy chỉnh collider nếu cần
        #self.collider = BoxCollider(self, center=Vec3(0, 1, 0), size=Vec3(1, 2, 1))

    def shoot(self):
        if self.gun:
            self.gun.shoot()