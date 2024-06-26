import turtle
from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
race_is_on=False

user_bet=screen.textinput(title="want to bet?",prompt="what's your color choice of the turtle?")

colors=["red","blue","orange","purple","green","black"]
y_coordinates = [-60,-30,0,30,60,90]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230,y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on=True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_is_on=False
            winning_color=turtle.pencolor()
            if turtle.pencolor()==user_bet:
                print("hurray!you won the bet")
            else:
                print(f"oops! {winning_color} won the race")

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
