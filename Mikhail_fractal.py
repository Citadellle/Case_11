import turtle as t
import ru_local as ru


def ice_fractal(length: float, n: int) -> None:
    '''
    The function draws an ice fractal using recursion.
    
    A complex, symmetrical pattern with 120° angles is created. At each level of recursion,
    segments are replaced by more detailed branching structures.
    
    Args:
        length: Current segment length
        n: Recursion depth
    
    Algorithm:
        n=0: draw straight line
        n>0: [half] -> left 120° -> [quarter] -> left 180° -> [quarter] -> 
             left 120° -> [quarter] -> left 180° -> [quarter] -> [quarter] -> 
             right 180° -> [quarter] -> right 120° -> [quarter] -> right 180° -> 
             [quarter] -> right 120° -> [half]
    '''
    if n == 0:
        t.fd(length)
        
    else:
        ice_fractal(length / 2, n - 1)
        t.lt(120)
        ice_fractal(length / 4, n - 1)
        t.lt(180)
        ice_fractal(length / 4, n - 1)
        t.lt(120)
        ice_fractal(length / 4, n - 1)
        t.lt(180)
        ice_fractal(length / 4, n - 1)
        ice_fractal(length / 4, n - 1)
        t.rt(180)
        ice_fractal(length / 4, n - 1)
        t.rt(120)
        ice_fractal(length / 4, n - 1)
        t.rt(180)
        ice_fractal(length / 4, n - 1)
        t.rt(120)
        ice_fractal(length / 2, n - 1)



def ice_snowflake(length: float, n: int, num_corn: int) -> None:
    '''
    The function draws a snowflake composed of ice fractal elements.
    
    Creates a symmetrical snowflake pattern by repeating the ice fractal
    with specified number of corners.
    
    Args:
        length: Segment length for fractal elements
        n: Recursion depth
        num_corn: Number of corners in the snowflake
    
    Algorithm:
        n = 0: draws a fractal from straight lines
        n > 0: draws a fractal from complex structures of ice fractals
    '''
    if n == 0:
        t.forward(length)
        for _ in range(num_corn - 1):
            t.right(360 // num_corn)
            t.forward(length)
    else:
        ice_fractal(length, n)
        for _ in range(num_corn):
            t.right(360 // num_corn)
            ice_fractal(length, n)

        
def main():
    n = int(input(ru.DEPTH))

    print(ru.MENU_MIKHAIL)
    option = int(input(ru.INPUT_QUESTION))
    
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
        t.speed(1)

    t.up()
    t.goto(-150, 150)
    t.down()

    if option == 0:
        ice_snowflake(300, n, 6)
    else:
        ice_snowflake(300, n, 3)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.done()


if __name__ == '__main__':
    main()
