#####code to extract rgb colors  from cologram ####
import turtle
# import colorgram
# colors=colorgram.extract('painting.jpg',20)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_colors=(r,g,b)
#     rgb_colors.append(my_colors)
# print (rgb_colors)

from turtle import Turtle,Screen
import random

color_list=[(148, 77, 56), (160, 54, 74), (206, 152, 105), (138, 28, 46), (65, 26, 36), (238, 213, 186), (62, 33, 26), (60, 89, 150), (243, 206, 79), (193, 95, 79), (196, 75, 93), (116, 41, 32), (74, 110, 208), (217, 150, 26), (193, 133, 144), (36, 41, 62), (99, 148, 212), (64, 112, 93), (46, 55, 108), (31, 48, 38)]

turtle.colormode(255)
tim=Turtle()

# tim.speed("fast")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots=100

for dot in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        
screen=Screen()
screen.exitonclick()
