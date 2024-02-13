from turtle import *


#we want to paint a house

speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)  

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)    

penup()
goto (200, 200)
pendown()

color("red")
right(150)
forward(200)
left(120)
forward(200)
color("brown")


penup()
goto(130,130)
pendown()

left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)

forward(60)
right(90)
forward(50)
right(90)
forward(60)

left(180)

forward(110)
left(90)
forward(50)
right(270)
forward(50)

exitonclick()



