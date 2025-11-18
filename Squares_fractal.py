import turtle as t

def draw_square_spiral(side_length, angle, depth):
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

    draw_square_spiral(side_length * 0.91, angle, depth - 1)


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

    draw_square_spiral(100, n, 45)

    # Спрятать курсор черепахи
    t.hideturtle()
    # Обновление окна с черепахой
    t.update()
    t.done()