import math
import boy


# 원 충돌 검사.
def Check_Collision(Dst, Src):
    if Dst.isDead:
        return False

    Distance = math.sqrt(pow(Dst.x - Src.x, 2) + pow(Dst.y - Src.y, 2))
    Sum_Radius = Dst.radius + Src.radius

    if Distance <= Sum_Radius:
        return True
    else:
        return False
    pass


def Collision_Boy_Ball(DstLst, SrcLst):
    # DstLst - Ball
    # SrcLst - Boy

    for Dst in DstLst:
        for Src in SrcLst:
            if Check_Collision(Dst, Src):
                Dst.isDead = True
                boy.ball_cnt += 1
                return True

    return False

    pass