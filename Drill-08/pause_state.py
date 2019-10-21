import game_framework
from pico2d import *
import main_state

image = None


def enter():
    global image
    image = load_image('pause.png')
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
            # p 버튼을 누르면 game_framework에서 pop_state
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    clear_canvas()

    image.clip_draw(230, 230, 430, 430, 400, 300)

    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass
