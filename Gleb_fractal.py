import turtle as t


def water_dragon(a: float, n: int) -> None:
    '''
    This function starts a recursive process with a depth of n:
    1.  The base of the recursion is a semicircle with radius a
    2.  Subsequent levels of recursion are semicircles
        on a quarter circle of the previous level
    3.  At the end of the program, it displays the
        "Water Dragon" pattern on the screen.
    :param a:
    :param n:
    :return None:
    '''
    x = [1] + [-1] * (n - 2) + [1]

    if n == 1:
        if x[n-1] > 0:
            t.rt(90)
            t.circle(a,180)
            t.rt(90)
        else:
            t.lt(90)
            t.circle(-a, 180)
            t.lt(90)

    else:
        t.left(45*x[n-1])
        x[n-2]*=-1
        water_dragon(a/2**(1/2), n-1)
        t.right(90*x[n-1])
        x[n-2]*=-1
        water_dragon((a / 2 ** (1 / 2)), n - 1)
        t.left(45*x[n-1])



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

    water_dragon(100, n)

    # Спрятать курсор черепахи
    t.hideturtle()
    # Обновление окна с черепахой
    t.update()
    t.done()