def main() -> None:
    import ru_local as ru
    import turtle as t
    import Gleb_fractal as gf
    import Ice_fractal_1 as ice1
    import Ice_fractal_2 as ice2
    import Koch_curve as kcruve
    import koch_snowflake as snow
    import Levy_curve as levy
    import Mikhail_fractal as mf
    import Minkowski_curve as mink
    import Sergey_fractal as sf
    import Squares_fractal as squares
    import Tree_fractal as tree
    '''
    This feature allows the user to select a fractal to draw,
    as well as the parameters for drawing fractals.
    '''
    choose_fractal = 11
    while choose_fractal not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(ru.MENU)
        choose_fractal = int(input(ru.INPUT_QUESTION))

    tracer_val = None
    while tracer_val not in [0, 1]:
        try:
            tracer_val = int(input(ru.ANIMATION))
            if tracer_val not in [0, 1]:
                print(ru.VALUE_ERROR)
        except:
            print(ru.VALUE_ERROR)

    if tracer_val == 1:
        # Отключение анимации рисования, не обновление экрана
        t.tracer(0)
    else:
        t.speed(400)

    deep = int(input(ru.DEEP))
    length = int(input(ru.LENGTH))

    try:
        match choose_fractal:
            case 0:
                tree.tree(length, deep)
            case 1:
                squares.draw_square_spiral(length, 0, deep)
            case 2:
                ice1.ice_fractal_1(length, deep)
            case 3:
                ice2.ice_fractal_2(length, deep)
            case 4:
                kcruve.koch(length, deep)
            case 5:
                snow.koch_snowflake(length, deep)
            case 6:
                levy.draw_levy_curve(length, deep)
            case 7:
                mink.minkowski_curve(length, deep)
            case 8:
                mf.minkowski_curve(length, deep)
            case 9:
                gf.water_dragon(length, deep)
            case 10:
                sf.spiral(length, deep)
    except RecursionError:
        print(ru.REC_ERROR)
    t.mainloop()


if __name__ == '__main__':
    main()
