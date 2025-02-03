from turtle import *

#we want to draw a house

#step 1:draw a square

speed(30)
width(7)
color("cyan")
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
color("magenta")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("orange")
begin_fill
right(150)
forward(200)
left(120)
forward(200)
end_fill()




exitonclick()

