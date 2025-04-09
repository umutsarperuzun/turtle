import turtle

drawing_board = turtle.Screen()
drawing_board.title("Turtle Drawing Board")
drawing_board.bgcolor("light blue")
turtle_instance = turtle.Turtle()

def star(side_length=100):
    for i in range(5):
        turtle_instance.left(216)
        turtle_instance.forward(side_length)
        
        

star()
    

turtle.done()



