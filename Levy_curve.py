import turtle as t


def draw_levy_curve(length: float, depth: int) -> None:
    """
    Recursively draws a Levy curve using the turtle module.
    :param length: the length of the segment at the current recursion level
    :param depth: the depth of the recursion
    """
    if depth == 0:
        t.forward(length)
    else:
        t.left(45)
        draw_levy_curve(length / (2 ** 0.5), depth - 1)
        t.right(90)
        draw_levy_curve(length / (2 ** 0.5), depth - 1)
        t.left(45)


def main():
    n = int(input('Введите глубину рекурсии: '))
    
    tracer_val = None
    while tracer_val not in [0, 1]:
        try:
            tracer_val = int(input('Отключить анимацию рисования или оставить? (1 - отключить; 0 - оставить) '))
            if tracer_val not in [0, 1]:
                print('Введите корректное значение')
        except:
            print('Введите корректное значение')

    if tracer_val == 1:
        # Отключение анимации рисования, не обновление экрана
        t.tracer(0)
    else:
        t.speed(400)

    t.up()
    t.goto(-500, 0)
    t.down()

    draw_levy_curve(100, n)

    # Спрятать курсор черепахи
    t.hideturtle()
    # Обновление окна с черепахой
    t.update()
    t.done()