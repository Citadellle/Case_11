import turtle as t
import ru_local as ru


def koch(size: float, order: int) -> None:
    if order == 0:
        t.forward(size)
    else:
        koch(size / 3, order - 1)
        t.left(60)
        koch(size / 3, order - 1)
        t.right(120)
        koch(size / 3, order - 1)
        t.left(60)
        koch(size / 3, order - 1)


def koch_snowflake(size, order):
    if order == 0:
        t.forward(size)
        for _ in range(2):
            t.right(120)
            t.forward(size)
    else:
        koch(size, order)
        for _ in range(3):
            t.right(120)
            koch(size, order)


def main():
    n = int(input(ru.DEEP))
    
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
    t.goto(-150, 150)
    t.down()

    koch_snowflake(300, n)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.done()


if __name__ == '__main__':
    main()
