from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
# character = load_image('run_animation.png')

character = load_image('animation_sheet.png')

x = 0
y = 90
frame = 0
bIsTurn = False
iDir = 100
count = 0
dstx = 203
dsty = 535
tempx = 203

# 여기를 채우세요.
def Cal_Degree(ax,bx,ay,by):
    w=ax-bx
    h=ay-by
    d=math.sqrt(pow(w,2)+pow(h,2))

    angle = math.acos(w/d)

    if(by > ay):
        angle = angle*-1

    return angle * 180.0 / math.pi

while True:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, iDir, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    if tempx < dstx:
        iDir=100
    elif tempx > dstx:
        iDir=0

    if(dstx - 3 <= x and x <= dstx + 3 and
       dsty - 3 <= y and y <= dsty + 3):
        tempx = dstx
        count+=1


    if count == 0:
        dstx=203
        dsty=535

    elif count == 1:
        dstx=132
        dsty=243

    elif count == 2:
        dstx=535
        dsty=470

    elif count == 3:
        dstx=477
        dsty=203

    elif count == 4:
        dstx=715
        dsty=136

    elif count == 5:
        dstx=316
        dsty=225

    elif count == 6:
        dstx = 510
        dsty = 92

    elif count == 7:
        dstx =692
        dsty = 518

    elif count == 8:
        dstx = 682
        dsty = 336

    elif count == 9:
        dstx = 712
        dsty = 349

    elif count == 10:
        count = -1

    myAngle = Cal_Degree(x,dstx,y,dsty)

    x-=math.cos(myAngle * math.pi / 180.0) * 5.0
    y-=math.sin(myAngle * math.pi / 180.0) * 5.0

    delay(0.05)
    get_events()

close_canvas()
