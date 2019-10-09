from pico2d import *
import math

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


# 각도 계산
def Cal_Degree(ax, bx, ay, by):
    w = ax - bx
    h = ay - by
    d = math.sqrt(pow(w, 2) + pow(h, 2))

    angle = math.acos(w / d)

    if by > ay:
        angle = angle * -1

    return angle * 180.0 / math.pi


# 마우스 이벤트
def handle_events():
    # fill here
    global running
    global x, y
    global tempx, tempy
    global bIsMove

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                tempx, tempy = event.x, KPU_HEIGHT - 1 - event.y
                bIsMove = True

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


# fill here
open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

movex, movey = KPU_WIDTH // 2, KPU_HEIGHT // 2
tempx, tempy = KPU_WIDTH // 2, KPU_HEIGHT // 2  # 마우스 값

frame = 0

hide_cursor()

myAngle = 0.0

bIsMove = False

dirx = tempx
dir = 100

while running:
    clear_canvas()

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.draw(x, y)

    character.clip_draw(frame * 100, dir, 100, 100, movex, movey)

    update_canvas()

    frame = (frame + 1) % 8

    delay(0.03)
    handle_events()

    dirx = movex

    if dirx < tempx:
        dir = 100
    elif dirx > tempx:
        dir = 0

    if (tempx - 3 <= movex <= tempx + 3 and
            tempy - 3 <= movey <= tempy + 3 and bIsMove == True):
        bIsMove = False

    if bIsMove == True:
        myAngle = Cal_Degree(movex, tempx, movey, tempy)
        movex -= math.cos(myAngle * math.pi / 180.0) * 5.0
        movey -= math.sin(myAngle * math.pi / 180.0) * 5.0

close_canvas()
