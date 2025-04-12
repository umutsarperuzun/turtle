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

# Turtle for display the countdown
count_writer = turtle.Turtle()
count_writer.hideturtle()
count_writer.penup()
count_writer.goto(0, 260)
count_writer.write(f"Time Left: {10 - click_count}", align="center", font=("Arial", 14, "normal"))

# Player turtle (the one to click)
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
        count_writer.clear()
        count_writer.write("Time's up!", align="center", font=("Arial", 14, "bold"))
        return

    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    player.goto(x, y)
    player.showturtle()

    click_count += 1

    # Update countdown display
    count_writer.clear()
    count_writer.write(f"Time Left: {10 - click_count}", align="center", font=("Arial", 14, "normal"))

    drawing_board.ontimer(hide_and_repeat, 1000)  # Hide after 1 second

# Hide the turtle and call show again
def hide_and_repeat():
    player.hideturtle()
    show_random_turtle()

player.onclick(increase_score)
show_random_turtle()


turtle.mainloop()

