import random
from turtle import Turtle, Screen

is_game_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your Bet :", prompt="How will win the race? color : ")
color_turtle = ["violet", "blue", "green", "yellow", "orange", "red"]
y_coordinate = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color_turtle[index])
    tim.penup()
    tim.goto(x=- 220, y=y_coordinate[index])
    all_turtles.append(tim)


def forward_move():
    move = random.randint(0, 10)
    return move


if user_bet:
    is_game_on = True


while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You're turtle won {winning_color}")
            else:
                print(f"You're turtle lost, {winning_color} won")

        turtle.fd(forward_move())

my_screen.exitonclick()
