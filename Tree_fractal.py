import turtle as t
import ru_local as ru


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
        t.fd(a)
        t.fd(-a)
    
    else:
        t.fd(3*a/4)
        t.rt(30)
        tree(2*a/3,n-1)
        t.lt(60)
        tree(2*a/3,n-1)
        t.rt(30)
        t.fd(-3*a/4)


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
    t.goto(0, 0)
    t.down()

    t.left(90)
    tree(100, n)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.done()


if __name__ == '__main__':
    main()
