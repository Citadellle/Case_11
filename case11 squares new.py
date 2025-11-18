import turtle
import math


def draw_square_spiral(t: turtle.Turtle, side_length: float, angle: float, depth: int) -> None:
    """
    Recursively draws a spiral of squares, twisting clockwise.,
    in this case, each subsequent square is shifted closer to the center.

    :param t: turtle object
    :param side_length: side length of the current square
    :param angle: angle of rotation between squares
    :param depth: number of squares
    """
    if depth <= 0:
        return

    for side1 in range(4):
        t.forward(side_length)
        t.right(90)

    t.right(angle)
    '''
    We move inwards — by a distance
    proportional to the side and angle
    '''
    step_inward = side_length * 0.1
    t.forward(step_inward)

    draw_square_spiral(t, side_length * 0.91, angle, depth - 1)


if __name__ == "__main__":
    while True:
        try:
            user_depth = int(input("Введите глубину рекурсии (количество квадратов): "))
            if user_depth > 0:
                break
            else:
                print("Глубина должна быть положительным числом. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Спираль из квадратов — ближе к центру")

    t = turtle.Turtle()
    t.speed(10)
    t.color("black")
    t.pensize(1)
    '''
    We start from the upper-left
    corner so that the spiral curls inwards
    '''
    t.penup()
    t.goto(-150, 150)
    t.pendown()

    draw_square_spiral(t, 300, 10, user_depth)

    t.hideturtle()
    screen.mainloop()