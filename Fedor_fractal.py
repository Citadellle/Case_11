import turtle as t

def draw_star(size: float) -> None:
    '''Draws a five-pointed star of the specified size
    
    The star is drawn starting from the current turtle position and heading,
    with each arm of the star having the given `size`. The turtle uses the
    standard angle of 144 degrees between edges to form a regular pentagram.
    
    Args:
        size (float): The length of each edge of the star.'''
    for _ in range(5):
        t.forward(size)
        t.right(144)

def recursive_star(size: float, depth: int) -> None:
    '''Recursively draws nested stars in the center of each other
    
    Each subsequent star is smaller (scaled by 0.6) and slightly shifted toward the center
    of the previous one to create a concentric visual effect. The recursion stops when
    the depth reaches zero or the star size becomes too small (less than 5 units).    
    Args:
        size (float): The size of the current star to draw.
        depth (int): The remaining recursion depth (number of nested stars to draw).'''
    if depth <= 0 or size < 5:
        return

    t.begin_fill()
    draw_star(size)
    t.end_fill()

    t.penup()
    t.left(90)          
    t.forward(size * 0.1)  
    t.right(90)         
    t.pendown()

    recursive_star(size * 0.6, depth - 1)

def main() -> None:
    t.speed(400)
    t.color('red')
    t.fillcolor('red')

    t.penup()
    t.goto(0, -100)  
    t.pendown()

    recursive_star(200, int(input()))  

    t.done()

if __name__ == '__main__':
    main()

