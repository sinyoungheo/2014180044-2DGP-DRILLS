import game_framework
from pico2d import *
import main_state

image = None


class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.switch = 0

    def draw(self):
        if self.switch == 1:
            self.image.clip_draw(230, 230, 430, 430, 400, 300)

    def update(self):
        self.switch = (self.switch + 1) % 2
        delay(0.05)


def enter():
    global image

    # 이미지를 클래스로 생성.
    image = Pause()
    pass


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            # p 버튼을 누르면 game_framework 에서 pop_state
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    clear_canvas()

    # main state에 있는 boy와 grass 랜더링
    main_state.boy.draw()
    main_state.grass.draw()

    # pause Logo 랜더링
    image.draw()

    update_canvas()

    pass


def update():
    image.update()
    pass


def pause():
    pass


def resume():
    pass
