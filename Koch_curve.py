import turtle as t
import ru_local as ru


def koch(size: float, order: int) -> None:
    '''
    Draws a Koch curve segment using recursion.
    
    The Koch curve is a fractal that starts with a straight line and recursively
    replaces each segment with a pattern of four smaller segments forming a "bump".
    At order 0, it draws a straight line. For higher orders, it divides the line
    into thirds and adds a triangular bump in the middle third.
    
    Args:
        size (float): The length of the current segment
        order (int): The recursion depth. When order is 0, draws a straight line.
    
    Returns:
        None
    '''
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


def main() -> None:
    '''
    Main function that sets up the turtle environment and draws a Koch curve.
    
    Handles user input for recursion depth and animation preferences,
    positions the turtle on the canvas, and initiates the Koch curve drawing.
    Provides options for instant rendering (tracer off) or animated visualization.
    
    The function positions the turtle at the left side of the screen and draws
    a Koch curve horizontally to the right.
    
    Returns:
        None
    '''
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

    koch(1000, n)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.done()


if __name__ == '__main__':
    main()

