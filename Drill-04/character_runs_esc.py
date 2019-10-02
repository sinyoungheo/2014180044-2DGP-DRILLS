from pico2d import *

open_canvas()
grass = load_image('grass.png')
# character = load_image('run_animation.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
bIsTurn = False
iDir = 100

# 여기를 채우세요.

while (True):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, iDir, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8

    if x >= 800:
        bIsTurn = True
    elif x <= 0:
        bIsTurn = False
    if bIsTurn == False:
        x = x + 5
        iDir = 100

    elif bIsTurn:
        x = x - 5
        iDir = 0

    delay(0.05)
    get_events()

close_canvas()