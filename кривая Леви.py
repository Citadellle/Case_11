import turtle

def draw_levy_curve(length, depth):
    """
    Recursively draws a Levy curve using the turtle module.
    :param length: the length of the segment at the current recursion level
:param depth: the depth of the recursion
    """
    if depth == 0:
        turtle.forward(length)
    else:
        turtle.left(45)
        draw_levy_curve(length / (2 ** 0.5), depth - 1)
        turtle.right(90)
        draw_levy_curve(length / (2 ** 0.5), depth - 1)
        turtle.left(45)


def main():
    turtle.speed("fastest")  
    turtle.penup()
    turtle.goto(-100, 0)     
    turtle.pendown()
    
    draw_levy_curve(200, 10)
    
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
