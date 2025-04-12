import turtle
import random

# Create the screen
drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Click the Turtle Game")

# Initialize score and appearance counter
score = 0
click_count = 0

# Turtle for display the score
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 300)
score_writer.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Player turtle 
player = turtle.Turtle()
player.shape("turtle")
player.shapesize(2, 2)  
player.color("green")
player.penup()
player.hideturtle()  

# Function called when the turtle is clicked
def increase_score(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Show the turtle at a random position
def show_random_turtle():
    global click_count
    if click_count >= 10:
        player.hideturtle()
        return

    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    player.goto(x, y)
    player.showturtle()

    click_count += 1
    drawing_board.ontimer(hide_and_repeat, 1000) 
    
# Hide turtle,call show function again
def hide_and_repeat():
    player.hideturtle()
    show_random_turtle()

# Bind click event and start the game
player.onclick(increase_score)
show_random_turtle()

turtle.mainloop()
