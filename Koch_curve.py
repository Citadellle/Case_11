import turtle as t


def koch(size: float, order: int) -> None:
    if order == 0:
        t.forward(size)
    else:
        koch(size / 3, order - 1)
        t.left(60)
        koch(size / 3, order - 1)
        t.right(120)
        koch(size / 3, order - 1)
        t.left(60)
        koch(size / 3, order - 1)


def main() -> None:
    t.up()
    t.goto(-100, 0)
    t.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(a, n)