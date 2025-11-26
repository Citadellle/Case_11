import turtle as t

def draw_star(size: float) -> None:
    '''Draws a five-pointed star of the specified size'''
    for _ in range(5):
        t.forward(size)
        t.right(144)

def recursive_star(size: float, depth: int) -> None:
    '''Recursively draws nested stars
        in the center of each other'''
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
