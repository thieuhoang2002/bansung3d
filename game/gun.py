from ursina import *
from game.bullet import Bullet  # Giả sử bạn có class Bullet để xử lý đạn

class Gun(Entity):
    def __init__(self, player, fire_rate=0.5, damage=10):
        # super().__init__(
        #     model='assets/models/gun/Beretta Pistol.fbx',  # Đường dẫn đến mô hình súng
        #     texture='assets/models/gun/gun_blue_violet_texture.png',  # Đường dẫn đến texture
        #     scale=(0.002, 0.002, 0.002),  # Điều chỉnh kích thước súng (thử nghiệm để phù hợp)
        #     parent=camera,  # Gắn súng vào camera để hiển thị trong góc nhìn thứ nhất
        #     #position=(0, -0.5, 1),  # Vị trí súng trên màn hình (góc dưới bên phải)
        #     position=(0.5, -0.25, 0.25),  # Đặt ở góc dưới bên phải
        #     rotation=(0, 0, 0),  # Xoay súng nếu cần
        #     # rotation=(0, 0, 0),
        #     origin_z=-0.5  # Điều chỉnh tâm của súng
        # )
        super().__init__(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.red, on_cooldown=False)
        self.player = player
        self.fire_rate = fire_rate  # Tốc độ bắn (ví dụ: 0.5 giây giữa các phát)
        self.damage = damage  # Sát thương của đạn
        self.last_shot = 0  # Thời điểm bắn cuối cùng
        self.ammo = 10  # Số đạn tối đa
        self.reloading = False

    def shoot(self):
            if self.reloading or self.ammo <= 0:
                return
            if time.time() - self.last_shot > self.fire_rate:
                self.last_shot = time.time()
                self.ammo -= 1
                bullet_start_position = self.world_position + self.forward * 0.5
                Bullet(position=bullet_start_position, direction=camera.forward, damage=self.damage)
                Audio('assets/sounds/lasergun.wav', autoplay=True)
                # Thêm recoil
                self.y += 0.002  # Nhích súng lên
                invoke(setattr, self, 'y', -0.5, delay=0.1)  # Trả lại vị trí ban đầu sau 0.1 giây
                if self.ammo <= 0:
                    self.reload()

    def reload(self):
            self.reloading = True
            Audio('assets/sounds/reload.mp3', autoplay=True)
            invoke(self.finish_reloading, delay=2)  # Nạp đạn trong 2 giây

    def finish_reloading(self):
        self.ammo = 10
        self.reloading = False