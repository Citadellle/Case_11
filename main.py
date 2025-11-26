import turtle as t

import ru_local as ru

import Squares_fractal
import Tree_fractal
import Koch_curve
import Koch_snowflake
import Minkowski_curve
import Ice_fractal_1
import Ice_fractal_2
import Levy_curve

import Mikhail_fractal
import Sergey_fractal
import Gleb_fractal


def main() -> None:
    '''
    This feature allows the user to select a fractal to draw,
    as well as the parameters for drawing fractals.
    '''
    choose_fractal = None
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
        # Disabling the drawing animation, not updating the screen
        t.tracer(0)
    else:
        t.speed(400)


    length = int(input(ru.LENGTH))
    depth = int(input(ru.DEPTH))  


    try:
        match choose_fractal:
            case 0:
                t.left(90)
                Tree_fractal.tree(length, depth)
                
            case 1:
                Squares_fractal.draw_square_spiral(length, depth)

            case 2:
                Ice_fractal_1.ice_fractal_1(length, depth)

            case 3:
                Ice_fractal_2.ice_fractal_2(length, depth)

            case 4:
                Koch_curve.koch(length, depth)

            case 5:
                Koch_snowflake.koch_snowflake(length, depth)

            case 6:
                Levy_curve.draw_levy_curve(length, depth)

            case 7:
                Minkowski_curve.minkowski_curve(length, depth)

            case 8:
                print(ru.MENU_MIKHAIL)
                num_corn = int(input(ru.INPUT_QUESTION))
                if num_corn == 0:
                    num_corn = 6
                else:
                    num_corn = 3
                Mikhail_fractal.ice_snowflake(length, depth, num_corn)

            case 9:
                Gleb_fractal.water_dragon(length, depth)

            case 10:
                Sergey_fractal.spiral(length, depth)

    except RecursionError:
        print(ru.REC_ERROR)

    # Hide the turtle cursor
    t.hideturtle()
    # Updating the turtle window
    t.update()
    t.mainloop()


if __name__ == '__main__':
    main()
