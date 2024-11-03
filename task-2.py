import math
import turtle


def draw_pythagorean_tree(level, length):
    if level == 0:
        turtle.forward(length)
        turtle.backward(length)
        return

    turtle.forward(length)

    turtle.left(45)
    draw_pythagorean_tree(level - 1, length * math.sqrt(2) / 2)
    turtle.right(45)

    turtle.right(45)
    draw_pythagorean_tree(level - 1, length * math.sqrt(2) / 2)
    turtle.left(45)

    turtle.backward(length)


if __name__ == "__main__":
    turtle.speed(3)
    turtle.left(90)
    turtle.color("red")

    draw_pythagorean_tree(5, 100)

    turtle.done()
