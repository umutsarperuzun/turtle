import turtle

drawing_board = turtle.Screen()
drawing_board.title("Turtle Drawing Board")
drawing_board.bgcolor("light blue")
turtle_instance = turtle.Turtle()

def shrink_squares(initial_size=300, count=20, shrink_by=20):
    size = initial_size
    for _ in range(count):
        for _ in range(4):
            turtle_instance.forward(size)
            turtle_instance.left(90)
        size -= shrink_by
        turtle_instance.penup()
        turtle_instance.goto(turtle_instance.xcor() + shrink_by / 2, turtle_instance.ycor() - shrink_by / 2)
        turtle_instance.pendown()

shrink_squares()

turtle.done()
