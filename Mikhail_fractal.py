import turtle as t


def minkowski_curve(length: float, n: int) -> None:
    if n == 0:
        t.fd(length)
    
    else:
        minkowski_curve(length / 4, n - 1)
        t.lt(90)
        minkowski_curve(length / 4, n - 1)
        t.rt(90)
        minkowski_curve(length / 4, n - 1)
        t.rt(90)
        minkowski_curve(length / 4, n - 1)
        minkowski_curve(length / 4, n - 1)
        t.lt(90)
        minkowski_curve(length / 4, n - 1)
        t.lt(90)
        minkowski_curve(length / 4, n - 1)
        t.rt(90)
        minkowski_curve(length / 4, n - 1)


def spiral(length, n):
    if n == 0:
        t.forward(length)

    else:
        minkowski_curve(length / 2, n - 1)
        t.lt(90)
        minkowski_curve(length / 3, n - 1)
        t.lt(90)
        minkowski_curve(length / 4, n - 1)
        t.lt(90)
        minkowski_curve(length / 5, n - 1)
        t.lt(90)
        minkowski_curve(length / 7, n - 1)

        


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
        t.speed(10)

    t.up()
    t.goto(-500, 0)
    t.down()

    spiral(1000, n)

    # Спрятать курсор черепахи
    t.hideturtle()
    # Обновление окна с черепахой
    t.update()
    t.done()