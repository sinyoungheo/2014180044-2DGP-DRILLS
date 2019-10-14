from pico2d import *
import random


# Game object class here

# 잔디
class CGrass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


# 소년
class CBoy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


# 축구공
class CBall:
    def __init__(self):
        # X 좌표는 10 ~ 790 Y 좌표는 700 고정
        self.x, self.y = random.randint(10, 790), 700

        # 0이면 21 크기, 1이면 41크기
        self.ball_size = random.randint(0, 1)

        if self.ball_size == 0:
            self.image = load_image('ball21x21.png')
        elif self.ball_size == 1:
            self.image = load_image('ball41x41.png')

        # 떨어지는 속도 5 ~ 20
        self.speed = random.randint(5, 20)

    def update(self):
        # 공의 크기가 21일 때
        if self.ball_size == 0:
            # 땅에 닿았다면 높이 고정.
            if self.y <= 64:
                self.y = 64
            else:
                self.y -= self.speed

        # 공이 크기가 41일 때
        elif self.ball_size == 1:
            # 땅에 닿았다면 높이 고정.
            if self.y <= 74:
                self.y = 74
            else:
                self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code


open_canvas()

team = [CBoy() for i in range(11)]
balls = [CBall() for j in range(20)]
grass = CGrass()

running = True

# game main loop code


while running:
    handle_events()

    for boy in team:
        boy.update()

    for ball in balls:
        ball.update()

    clear_canvas()

    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw()

    grass.draw()
    update_canvas()

    delay(0.05)

# finalization code


close_canvas()
