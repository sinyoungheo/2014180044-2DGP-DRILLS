import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     ' + str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


# 3개의 점을 통한 곡선.
def draw_curve_3_points(p1, p2, p3):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)

    for i in range(0, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

        draw_point((x, y))

    draw_point(p3)
    pass


# 4개의 점을 통한 곡선.
def draw_curve_4_points(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        draw_point((x, y))
    draw_point(p2)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        draw_point((x, y))
    draw_point(p3)

    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p2[0] + (-4 * t ** 2 + 4 * t) * p3[0] + (2 * t ** 2 - t) * p4[0]
        y = (2 * t ** 2 - 3 * t + 1) * p2[1] + (-4 * t ** 2 + 4 * t) * p3[1] + (2 * t ** 2 - t) * p4[1]
        draw_point((x, y))
    draw_point(p4)


def draw_curve_4_points_remake(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    # draw p1-p2
    for i in range(0, 50, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        draw_point((x, y))
    draw_point(p2)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        draw_point((x, y))
    draw_point(p3)

    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p2[0] + (-4 * t ** 2 + 4 * t) * p3[0] + (2 * t ** 2 - t) * p4[0]
        y = (2 * t ** 2 - 3 * t + 1) * p2[1] + (-4 * t ** 2 + 4 * t) * p3[1] + (2 * t ** 2 - t) * p4[1]
        draw_point((x, y))
    draw_point(p4)

    # draw p4-p5
    for i in range(50, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p3[0] + (-4 * t ** 2 + 4 * t) * p4[0] + (2 * t ** 2 - t) * p1[0]
        y = (2 * t ** 2 - 3 * t + 1) * p3[1] + (-4 * t ** 2 + 4 * t) * p4[1] + (2 * t ** 2 - t) * p1[1]
        draw_point((x, y))
    draw_point(p4)


def draw_curve_5_points(p1, p2, p3, p4, p5):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)
    draw_big_point(p5)

    # draw p1-p2
    for i in range(0, 100, 2):
        t = i / 100

        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2

        draw_point((x, y))

    draw_point(p2)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100

        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2

        draw_point((x, y))

    draw_point(p3)

    # draw p3-p4
    for i in range(0, 100, 2):
        t = i / 100

        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2

        draw_point((x, y))

    draw_point(p4)

    # draw p4-p5
    for i in range(0, 100, 2):
        t = i / 100

        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p2[1]) / 2

        draw_point((x, y))

    draw_point(p1)


def draw_start_end(p1, p2, p3, near, far):
    for i in range(near, far, 2):
        t = i / 100

        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

        draw_point((x, y))


def draw_middle(p1, p2, p3, p4, near, far):
    for i in range(near, far, 2):
        t = i / 100

        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2

        draw_point((x, y))


def draw_curve_11_points(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    global way
    # draw p1-p2
    draw_middle(p10, p1, p2, p3, 0, 100)

    # draw p2-p3
    draw_middle(p1, p2, p3, p4, 0, 100)

    # draw p3-p4
    draw_middle(p2, p3, p4, p5, 0, 100)

    # draw p4-p5
    draw_middle(p3, p4, p5, p6, 0, 100)

    # draw p5-p6
    draw_middle(p4, p5, p6, p7, 0, 100)

    # draw p6-p7
    draw_middle(p5, p6, p7, p8, 0, 100)

    # draw p7-p8
    draw_middle(p6, p7, p8, p9, 0, 100)

    # draw p8-p9
    draw_middle(p7, p8, p9, p10, 0, 100)

    # draw p9-p10
    draw_middle(p8, p9, p10, p1, 0, 100)

    # draw p10-p11
    draw_middle(p9, p10, p1, p2, 0, 100)


prepare_turtle_canvas()

# 10개의 랜덤한 점 지정.
point = [(random.randint(0, 300), random.randint(-300, 0)) for i in range(10)]

while True:
    draw_curve_11_points(point[0], point[1], point[2], point[3], point[4], point[5], point[6], point[7], point[8], point[9])

turtle.done()
