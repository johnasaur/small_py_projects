import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width = 500, height = 400)
user_bet= screen.textinput(title = "Make your bet", prompt="which turtle will win, enter a color: ")
print(user_bet)

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.color("yellow")
# tim.goto(x=-230, y=-100)
#
# tina = Turtle(shape="turtle")
# tina.penup()
# tina.color("orange")
# tina.goto(x=-230, y=-60)
#
# tank = Turtle(shape="turtle")
# tank.penup()
# tank.color("red")
# tank.goto(x=-230, y=-20)
#
# travis = Turtle(shape="turtle")
# travis.penup()
# travis.color("purple")
# travis.goto(x=-230, y=20)
#
# tony = Turtle(shape="turtle")
# tony.penup()
# tony.color("blue")
# tony.goto(x=-230, y=60)
#
# #in honor of Ireland - Taoiseach means Prime Minister :)
# taoiseach = Turtle(shape="turtle")
# taoiseach.penup()
# taoiseach.color("green")
# taoiseach.goto(x=-230, y=100)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40,-10,20,50,80]
is_race_on = False
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won by choosing {winning_color} color!")
            else:
                print(f"you lost, color {winning_color} won!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()

# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(key = "space", fun=move_forwards)


