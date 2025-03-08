from ursina import *

def create_environment():
    # Tạo sàn
    ground = Entity(
        model='plane',          # Mô hình là mặt phẳng
        scale=(50, 1, 50),     # Kích thước lớn
        texture='grass',        # Hình ảnh nền (cần file grass.png trong thư mục assets)
        collider='box'          # Hình dạng va chạm
    )
    # Tạo tường phía trước
    wall1 = Entity(
        model='cube',           # Mô hình là khối lập phương
        scale=(50, 10, 1),     # Kích thước
        position=(0, 5, 25),   # Vị trí
        texture='brick',        # Hình ảnh tường (cần file brick.png)
        collider='box'
    )
    # Tạo tường phía sau
    wall2 = Entity(
        model='cube',
        scale=(50, 10, 1),
        position=(0, 5, -25),
        texture='brick',
        collider='box'
    )
    # Có thể thêm các vật thể khác như chướng ngại vật ở đây