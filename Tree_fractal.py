import turtle as t
import ru_local as ru


def spiral(size, order):
    if order == 0:
        t.forward(size)
    else:
        spiral(size / 2, order - 1)
        t.right(90)
        spiral(size / 3, order - 1)
        t.right(90)
        spiral(size / 4, order - 1)
        t.right(90)
        spiral(size / 5, order - 1)


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
    t.goto(-500, 250)
    t.down()

    spiral(1000, n)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.done()


if __name__ == '__main__':
    main()
