from ursina import *
from game.player import Player

class Bullet(Entity):
    def __init__(self, position, direction, damage=10, speed=100):
        super().__init__(
            model='sphere',      # Mô hình đạn là hình cầu
            scale=0.6,           # Kích thước nhỏ
            color=color.yellow,  # Màu sắc
            position=position,   # Vị trí xuất phát
            collider='sphere'    # Hình dạng va chạm
        )
        self.direction = direction.normalized()  # Hướng di chuyển (chuẩn hóa)
        self.damage = damage                     # Sát thương của đạn
        self.speed = speed                       # Tốc độ di chuyển

    def update(self):
        # Di chuyển đạn theo hướng
        self.position += self.direction * self.speed * time.dt

        # Kiểm tra va chạm với người chơi
        hit_info = self.intersects()
        if hit_info.hit and isinstance(hit_info.entity, Player):
            hit_info.entity.take_damage(self.damage)
            destroy(self)  # Xóa đạn khi trúng mục tiêu

        # Xóa đạn nếu đi quá xa (tránh lãng phí tài nguyên)
        if self.position.length() > 100:
            destroy(self)