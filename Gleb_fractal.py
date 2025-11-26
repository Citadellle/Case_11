import turtle as t
import ru_local as ru


def water_dragon(a: float, n: int, x: list) -> None:
    '''
    This function starts a recursive process with a depth of n:
    1.  The base of the recursion is a semicircle with radius a
    2.  Subsequent levels of recursion are semicircles
        on a quarter circle of the previous level
    3.  At the end of the program, it displays the
        "Water Dragon" pattern on the screen.
    :param a:
    :param n:
    :param x:
    :return None:
    '''

    if n == 1:
        if x[n - 1] > 0:
            t.rt(90)
            t.circle(a, 180)
            t.rt(90)
        else:
            t.lt(90)
            t.circle(-a, 180)
            t.lt(90)

    else:
        t.left(45 * x[n - 1])
        x[n - 2] *= -1
        water_dragon(a / 2 ** (1 / 2), n - 1, x)
        t.right(90 * x[n - 1])
        x[n - 2] *= -1
        water_dragon((a / 2 ** (1 / 2)), n - 1, x)Q
        t.left(45 * x[n - 1])


def main():
    n = int(input(ru.DEPTH))

    tracer_val = None
    while tracer_val not in [0, 1]:
        try:
            tracer_val = int(input(ru.ANIMATION))
            if tracer_val not in [0, 1]:
                print(ru.VALUE_ERROR)
        except:
            print(ru.VALUE_ERROR)

    if tracer_val == 1:
        # Disabling the drawing animation, not updating the screen
        t.tracer(0)
    else:
        t.speed(400)

    t.up()
    t.goto(-100, 0)
    t.down()
    # List for rotation.
    x = [1] + [-1] * (n - 2) + [1]
    water_dragon(100, n, x)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.done()


if __name__ == '__main__':
    main()
