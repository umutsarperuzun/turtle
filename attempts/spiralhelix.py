import turtle

drawing_board = turtle.Screen()
drawing_board.title("Turtle Drawing Board")
drawing_board.bgcolor("light blue")
turtle_instance = turtle.Turtle()

turtle_instance.color("red")

turtle_colors = ["red", "green" , "yellow" , "blue" , "purple"]
def circle(c_angle):
    for i in range(20):
        turtle_instance.color(turtle_colors[i % 5])
        turtle_instance.circle(c_angle)
        c_angle-=20
        
        
circle(100)


turtle.mainloop()
    