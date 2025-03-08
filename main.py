from ursina import *
from game.player import Player
from game.gun import Gun
from game.environment import create_environment
from game.map import Map  # Import class Map

app = Ursina()

# Tạo bầu trời trong xanh
sky = Sky(color=color.clear)  # Màu xanh trong

# Tạo map
map = Map()

# # Tạo môi trường
# create_environment()

# Tạo một người chơi duy nhất
player = Player()
player.gun = Gun(player)

# def update():
#     pass

def input(key):
    if key == 'left mouse down':
        player.shoot()

app.run()