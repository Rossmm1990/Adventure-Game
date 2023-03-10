class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Finished:
    
    def enter(self):
        print("You did it the end!!")

class Beginning:
    
    def enter(self):
        print("You did it!!")
        return "death"

class Death:
    def enter(self):
        print("You died.")
        return "finished"

class Map:

    scenes = {
        'beginning': Beginning(),
        'finished': Finished(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

        
a_map = Map('beginning')
a_game = Engine(a_map)

a_game.play()



