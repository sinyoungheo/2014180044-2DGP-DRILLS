import random
from pico2d import *
import game_world
import game_framework


class Ball:
    image = None

    def __init__(self, background):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, = random.randint(0, 1600),  random.randint(0, 1200)
        self.bg = background

        self.radius = 10
        self.isDead = False

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        if self.isDead:
            return

        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom

        self.image.draw(cx, cy)
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def stop(self):
        pass