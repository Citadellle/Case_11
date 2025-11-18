import turtle as t

def tree(a: float, n: int) -> None:
    '''
    This function starts a recursive process with a depth of n:
    1.  The base of recursion is a segment of long a
    2.  Subsequent levels of recursion - 2 shorter segments
        extending from the end of the segments of the previous
        level at angles of 30 degrees
    3.  At the end of the program, it displays the
        "Ice Fractal" pattern on the screen.
    :param a:
    :param n:
    :return None:
    '''
    if n==0:
        t.fd(a)
        t.fd(-a)
    else:
        t.fd(3*a/4)
        t.rt(30)
        tree(2*a/3,n-1)
        t.lt(60)
        tree(2*a/3,n-1)
        t.rt(30)
        t.fd(-3*a/4)


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

    t.left(90)
    tree(100, n)

    # Спрятать курсор черепахи
    t.hideturtle()
    # Обновление окна с черепахой
    t.update()
    t.done()