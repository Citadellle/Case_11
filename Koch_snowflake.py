import turtle as t
import ru_local as ru


def koch(size: float, order: int) -> None:
    '''
    Draws a Koch curve segment using recursion.
    
    The Koch curve is a fractal that starts with a straight line and recursively
    replaces each segment with a pattern of four smaller segments forming a "bump".
    
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


def koch_snowflake(size, order):
    '''
    Draws a complete Koch snowflake by combining three Koch curves.
    
    The Koch snowflake is formed by drawing three Koch curves in a triangular pattern,
    creating a closed fractal shape with infinite perimeter but finite area.
    
    Args:
        size (float): The size/length of each side of the snowflake
        order (int): The recursion depth for the Koch curves
    
    Returns:
        None
    '''
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


def main() -> None:
    '''
    Main function that sets up the turtle environment and draws a Koch snowflake.
    
    Handles user input for recursion depth and animation preferences,
    positions the turtle on the canvas, and initiates the snowflake drawing.
    Provides options for instant rendering or animated visualization.
    
    Returns:
        None
    '''
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
