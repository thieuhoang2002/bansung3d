from ursina import *
from game.mapData.CustomLib import *  
from game.mapData.CubePositionData import listCubePosition
from game.mapData.WallPositionData import listWallPosition
from game.mapData.TreePositionData import listTreePosition
from game.mapData.HousePositionData import listHousePosition

class Map(Entity):
    def __init__(self):
        super().__init__()
        self.step = 5
        
        # Tạo mặt phẳng lớn làm nền
        self.ground = Entity(
            model='plane',
            scale=(3500, 1, 3500),
            texture='grass',  # Thay 'brick' bằng 'grass' để trông tự nhiên hơn
            collider='box',
            color=color.gray
        )
        
        # Tạo các đối tượng từ dữ liệu
        self.cubes = [createMyCube(pos['x'], pos['z'], pos['height'], pos['color']) for pos in listCubePosition]
        self.walls = [createWall(pos['x'], pos['z'], pos['width'], pos['height'], pos['color'], pos['corner']) for pos in listWallPosition]
        self.trees = [createTree(tree['x'], tree['z']) for tree in listTreePosition]
        self.houses = [createHouse(house['x'], house['z'], house['corner']) for house in listHousePosition]
        
        # Tạo creativeCube để debug hoặc xây dựng map
        self.creativeCube = createMyCube(-800, 0, 20, color.red)

    def input(self, key):
        if key == 'w':
            self.creativeCube.z += self.step
        if key == 's':
            self.creativeCube.z -= self.step
        if key == 'a':
            self.creativeCube.x -= self.step
        if key == 'd':
            self.creativeCube.x += self.step
        if key == 'space':
            print("cube:", "{", f"'x':{self.creativeCube.x}, 'height':20, 'z':{self.creativeCube.z}, 'color':color.green", "},")
            print("wall:", "{", f"'x':{self.creativeCube.x}, 'height':80, 'width':150, 'z':{self.creativeCube.z}, 'color':color.rgb(128, 49, 4), 'corner':0 ", "},")
            print("tree:", "{", f"'x':{self.creativeCube.x}, 'z':{self.creativeCube.z}", "},")
            print("house:", "{", f"'x':{self.creativeCube.x}, 'z':{self.creativeCube.z}, 'corner':0", "},")
            print("building:",
                  "{", f"'x':{self.creativeCube.x-60}, 'height':80*2, 'width':150*2, 'z':{self.creativeCube.z+200}, 'color':color.rgb(145, 117, 6), 'corner':0 ", "},",
                  "{", f"'x':{self.creativeCube.x+200}, 'height':80*2, 'width':150*3, 'z':{self.creativeCube.z-60}, 'color':color.rgb(145, 117, 6), 'corner':90 ", "},",
                  "{", f"'x':{self.creativeCube.x}, 'height':80*2, 'width':150*2+100, 'z':{self.creativeCube.z-260}, 'color':color.rgb(145, 117, 6), 'corner':0 ", "},",
                  "{", f"'x':{self.creativeCube.x-200}, 'height':80*2, 'width':150*2, 'z':{self.creativeCube.z+50}, 'color':color.rgb(145, 117, 6), 'corner':90 ", "},",
                  )