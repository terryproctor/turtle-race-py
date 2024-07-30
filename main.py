from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    rnd = random.randint(0, len(turtles) - 1)
    t = turtles[rnd]
    random_distance = random.randint(0, 10)
    t.forward(random_distance)
    if t.xcor() > 200:
        if t.pencolor() == user_bet:
            print(f"You've won! The {t.pencolor()} turtle is the winner!")
        else:
            print(f"You've lost! The {t.pencolor()} turtle is the winner")
        is_race_on = False

screen.exitonclick()
