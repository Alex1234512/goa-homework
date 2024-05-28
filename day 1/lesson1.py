from turtle import *

#we want to paint house

#step 1:   draw a square
speed(20)
width(7)
color("blue")
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
color("black")
left(90)
forward(80)     #height of the door
right(90)
forward(60)
right(90)
forward(80)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("blue")
penup()
goto(60, 160)
pendown()
left(30)

color("brown")

right(90)
forward(60)

penup()
goto(60, 160)
pendown()

left(90)
forward(60)
right(90)
forward(55)

penup()
goto(30, 160)
pendown()

left(90)
forward(60)

penup()
goto(60, 130)
pendown()

right(90)
forward(60)

penup()
goto(0, 0)
pendown()

right(90)

color("blue")

forward(200)

penup()
goto(200, 200)
pendown()

forward(1)

color("brown")

penup()
goto(200, 160)
pendown()

left(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)

penup()
goto(200, 200)
pendown()

color("blue")

right(90)
forward(200)

right(90)
forward(200)

penup()
goto(200,130)
pendown()

color("brown")

forward(60)

penup()
goto(170,130)
pendown()

right(90)
forward(30)

right(90)

right(90)
forward(60)

penup()
goto(200,200)
pendown()

color("blue")

forward(200)














exitonclick()


