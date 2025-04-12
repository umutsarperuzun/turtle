import turtle


# Create the screen
drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Click the Turtle Game")

grid_size = 15
def make_turtle(x,y):
    t=turtle.Turtle()
    t.shape("turtle")
    t.penup()
    t.shapesize(2,2)
    t.goto(x * grid_size,y * grid_size)
    
x_coordinate = [-20,-10,0,10,20]
y_coordinate = [20,10,0,-10]

for x in x_coordinate:
    for y in y_coordinate:
        make_turtle(x,y)
    
    


turtle.mainloop()