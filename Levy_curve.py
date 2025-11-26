import turtle as t
import ru_local as ru


def draw_levy_curve(length: float, depth: int) -> None:
    """
    Recursively draws a Levy curve using the turtle module.
    :param length: the length of the segment at the current recursion level
    :param depth: the depth of the recursion
    """
    if depth == 0:
        t.forward(length)
    else:
        t.left(45)
        draw_levy_curve(length / (2 ** 0.5), depth - 1)
        t.right(90)
        draw_levy_curve(length / (2 ** 0.5), depth - 1)
        t.left(45)


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
    t.goto(-50, 0)
    t.down()

    draw_levy_curve(100, n)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.done()


if __name__ == '__main__':
    main()

