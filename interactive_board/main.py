import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")


turtle_instance = turtle.Turtle()


drawing_board.listen()

def move_forward():
    turtle_instance.forward(50)
    
def turn_left():
    turtle_instance.setheading(turtle_instance.heading()-30)

def turn_right():
    turtle_instance.setheading(turtle_instance.heading()+30)
    
def clear_screen():
    turtle_instance.clear()
    
def back_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()
    
drawing_board.onkey(move_forward,"space")
drawing_board.onkey(turn_left,"Up")    
drawing_board.onkey(turn_right,"Down") 
drawing_board.onkey(clear_screen,"q")
drawing_board.onkey(back_home,"h")


     

turtle.mainloop()