import turtle as t


def spiral(size, order):
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

    spiral(1000, n)

    # Спрятать курсор черепахи
    t.hideturtle()
    # Обновление окна с черепахой
    t.update()
    t.done()