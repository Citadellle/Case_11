import turtle as t
import ru_local as ru


def ice_fractal_1(length: float, n: int) -> None:
    '''   
    The function draws a fractal ice crystal using recursion.
    At each level of recursion, segments are replaced by more complex structures.
    
    Args:
        length: Current segment length
        n: Recursion depth
    
    Algorithm:
        n=0: draw straight line
        n>0: [half segment] -> left 90° -> [quarter] -> right 180° -> 
             [quarter] -> left 90° -> [half segment]
    '''
    if n == 0:
        t.fd(length)
    
    else:
        ice_fractal_1(length / 2, n - 1)
        t.lt(90)
        ice_fractal_1(length / 4, n - 1)
        t.rt(180)
        ice_fractal_1(length / 4, n - 1)
        t.lt(90)
        ice_fractal_1(length / 2, n - 1)


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
    t.goto(-500, 0)
    t.down()

    ice_fractal_1(1000, n)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.done()


if __name__ == '__main__':
    main()
