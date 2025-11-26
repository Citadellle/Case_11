import turtle as t
import ru_local as ru


def minkowski_curve(length: float, n: int) -> None:
    '''
    The function draws a fractal of the Minkowski curve using recursion.
    
    A complex, asymmetrical pattern is created. At each level of recursion,
    segments are replaced by more detailed structures.
    
    Args:
        length: Current segment length
        n: Recursion depth
    
    Algorithm:
        n=0: draw straight line
        n>0: [quarter] -> left 90° -> [quarter] -> right 90° -> [quarter] -> 
             right 90° -> [quarter] -> [quarter] -> left 90° -> [quarter] -> 
             left 90° -> [quarter] -> right 90° -> [quarter]
    '''
    if n == 0:
        t.fd(length)
        
    else:
        minkowski_curve(length / 4, n - 1)
        t.lt(90)
        minkowski_curve(length / 4, n - 1)
        t.rt(90)
        minkowski_curve(length / 4, n - 1)
        t.rt(90)
        minkowski_curve(length / 4, n - 1)
        minkowski_curve(length / 4, n - 1)
        t.lt(90)
        minkowski_curve(length / 4, n - 1)
        t.lt(90)
        minkowski_curve(length / 4, n - 1)
        t.rt(90)
        minkowski_curve(length / 4, n - 1)

        
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
    t.goto(-500, 0)
    t.down()

    minkowski_curve(1000, n)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.done()


if __name__ == '__main__':
    main()
