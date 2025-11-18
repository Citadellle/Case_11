from turtle import *


def water_dragon(a: float, n: int) -> None:
    '''
    This function starts a recursive process with a depth of n:
    1.  The base of the recursion is a semicircle with radius a
    2.  Subsequent levels of recursion are semicircles
        on a quarter circle of the previous level
    3.  At the end of the program, it displays the
        "Water Dragon" pattern on the screen.
    :param a:
    :param n:
    :return None:
    '''
    if n == 1:
        if x[n-1] > 0:
            rt(90)
            circle(a,180)
            rt(90)
        else:
            lt(90)
            circle(-a, 180)
            lt(90)
        print(x[n-1])
    else:

        left(45*x[n-1])
        x[n-2]*=-1
        water_dragon(a/2**(1/2), n-1)
        right(90*x[n-1])
        x[n-2]*=-1
        water_dragon((a / 2 ** (1 / 2)), n - 1)
        left(45*x[n-1])


def ice_fractal(a: float, n: int) -> None:
    '''
    This function starts a recursive process with a depth of n:
    1.  The base of recursion is a segment of long a
    2.  Subsequent levels of recursion - 2 segments of half
        the length coming out of the center of the segments of
        the previous level at angles of 60 degrees
    3.  At the end of the program, it displays the
        "Ice Fractal" pattern on the screen.
    :param a:
    :param n:
    :return None:
    '''
    if n == 0:
        fd(a)
    else:
        ice_fractal(a/2,n-1)
        lt(120)
        ice_fractal(a/4,n-1)
        lt(180)
        ice_fractal((a/4),n-1)
        lt(120)
        ice_fractal(a / 4, n - 1)
        lt(180)
        ice_fractal((a / 4), n - 1)
        lt(120)
        ice_fractal(a/2,n-1)


def tree(a: float, n: int) -> None:
    '''
    This function starts a recursive process with a depth of n:
    1.  The base of recursion is a segment of long a
    2.  Subsequent levels of recursion - 2 shorter segments
        extending from the end of the segments of the previous
        level at angles of 30 degrees
    3.  At the end of the program, it displays the
        "Ice Fractal" pattern on the screen.
    :param a:
    :param n:
    :return None:
    '''
    if n==0:
        fd(a)
        fd(-a)
    else:
        fd(3*a/4)
        rt(30)
        tree(2*a/3,n-1)
        lt(60)
        tree(2*a/3,n-1)
        rt(30)
        fd(-3*a/4)

a = int(input())
n = int(input())
x = [1] + [-1] * (n - 2) + [1]

