import turtle as t
import ru_local as ru


def spiral(size: float, order: int) -> None:
    '''
    Draws a recursive spiral pattern using turtle graphics.
    
    The function creates a spiral by recursively drawing smaller segments
    at right angles to each other. Each recursive level reduces the size
    of the segments according to specific fractions.
    
    Args:
        size (float): The base size/length of the spiral segments
        order (int): The recursion depth. Higher orders create more complex spirals.
                    When order reaches 0, the function draws a straight line.
    
    Returns:
        None
    '''
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


def main() -> None:
    '''
    Main function that sets up the turtle environment and draws the spiral.

    
    This function handles user input for recursion depth and animation preferences,
    configures the turtle graphics window, positions the turtle, and initiates
    the spiral drawing process.
    
    The function provides two visualization modes:
    - Instant rendering (tracer off) for faster drawing
    - Animated rendering for watching the drawing process
    
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

