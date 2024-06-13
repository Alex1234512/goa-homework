from turtle import *

# we want to paint palace

#step 1:  drawing the palace

speed(300)
width(7)
color("black")

penup()
goto(200, 200)
pendown()

right(90)
forward(300)

right(90)
forward(700)

right(90)
forward(300)

right(45)
forward(120)

right(90)
forward(120)

right(45)
forward(60)

left(90)
forward(360)

left(90)
forward(60)

right(45)
forward(120)

right(90)
forward(120)

penup()
goto(200, 200)
pendown()

right(45)
forward(300)

right(180)
forward(30)

right(90)

#step 2: drawing the field

color("green")

forward(400)

penup()
goto(-500, 200)
pendown()

color("black")

right(90)
forward(270)

color("green")

begin_fill()

right(90)
forward(100)

left(90)
forward(250)

left(90)
forward(1200)

left(90)
forward(252)

end_fill()

#step 3: drawing the door

color("black")

penup()
goto(200, 200)
pendown()

left(180)
forward(300)

right(90)
forward(700)

right(90)
forward(39)

penup()
goto(-230, 0)
pendown()

right(90)
forward(160)

right(90)
forward(100)

penup()
goto(-230, 0)
pendown()

forward(100)

penup()
goto(-150, 0)
pendown()

forward(100)

#coloring the left door

color("brown")
begin_fill()
right(90)
forward(5)

right(90)
forward(93)

left(90)
forward(70)

left(90)
forward(93)

left(90)
forward(65)
end_fill()

#coloring the right door

begin_fill()
forward(85)

left(90)
forward(93)

left(90)
forward(75)

left(90)
forward(93)
end_fill()

color("black")

left(90)
forward(77)

left(180)
forward(80)

right(90)
forward(100)

left(180)
forward(100)

right(90)
forward(78)

right(90)
forward(100)

penup()
goto(-300, 140)
pendown()

left(90)
forward(30)

right(90)
forward(60)

#step 4: coloring the left roof

color("red")
begin_fill()
left(45)
forward(120)

left(90)
forward(120)

left(135)
forward(167)
end_fill()

#coloring the right roof

color("black")

penup()
goto(30, 140)
pendown()
begin_fill()
left(90)
forward(60)

color("red")

right(45)
forward(120)

right(90)
forward(120)

right(135)
forward(167)
end_fill()

color("red")

forward(3)


#step 5: coloring the palace

color("grey")
begin_fill()
left(90)
forward(60)

right(90)
forward(360)

right(90)
forward(55)

left(90)
forward(170)

left(90)
forward(295)

left(90)
forward(269)

left(90)
forward(100)

right(90)
forward(162)

right(90)
forward(100)

left(90)
forward(270)


left(90)
forward(300)

left(90)
forward(170)
end_fill()

forward(1)

left(90)
forward(300)

right(90)
forward(100)

color("black")

right(90)
forward(100)

left(90)
forward(155)

left(90)
forward(100)

#step 6: drawing the flag

color("grey")

penup()
goto(-300, 140)
pendown()

left(90)
forward(147)

color("black")
begin_fill()
left(90)
forward(150)

right(90)
forward(100)

right(90)
forward(80)

right(90)
forward(100)
end_fill()
penup()
goto(-140, 260)
pendown()

#step 7: painting GOA in the flag

color("white")

width(4)

right(180)
forward(15)

right(180)
forward(15)

left(90)
forward(20)

left(90)
forward(15)

left(90)
forward(10)

left(90)
forward(5)

penup()
goto(-130, 140)
pendown()

color("grey")

forward(30)

color("green")

width(4)

penup()
goto(-105, 240)
pendown()

color("green")

right(90)
forward(20)

right(90)
forward(10)

right(90)
forward(20)

right(90)
forward(10)

penup()
goto(-80, 240)
pendown()

color("white")

right(115)
forward(20)

right(130)
forward(20)

right(180)
forward(7)

left(70)
forward(10)

penup()
goto(-130, 140)
pendown()

width(7)

color("grey")

left(90)
forward(1)

right(90)
forward(50)

penup()
goto(600, 200)
pendown()

#step 8: drawing the sky

color("skyblue")

begin_fill()
left(85)
forward(265)

right(90)
forward(393)

right(90)
forward(268)

left(45)
forward(129)

left(90)
forward(129)

left(45)
forward(56)

right(90)
forward(172)

right(90)
forward(57)

right(90)
forward(101)

left(90)
forward(92)

left(90)
forward(113)

left(90)
forward(150)

right(90)
forward(165)

right(90)
forward(55)

left(45)
forward(127)

left(90)
forward(131)

left(45)
forward(264)

right(90)
forward(93)

right(90)
forward(400)

right(90)
forward(1200)

right(90)
forward(150)
end_fill()

#step 9: drawing the first window

penup()
goto(150, 100)
pendown()

color("brown")

forward(80)

right(90)
forward(60)

right(90)
forward(80)

penup()
goto(120, 100)
pendown()

right(90)
forward(30)

right(180)
forward(60)

right(180)
forward(60)

right(90)
forward(27)

right(90)
forward(60)

left(90)
forward(27)

left(90)
forward(60)

penup()
goto(150, 100)
pendown()

#step 10: drawing the second window
penup()
goto(-390, 100)
pendown()

right(90)
forward(80)

right(90)
forward(60)

right(90)
forward(80)

right(90)
forward(60)

right(90)
forward(27)

right(90)
forward(60)

left(90)
forward(27)

left(90)
forward(60)

right(90)
forward(26)

right(90)
forward(30)

right(90)
forward(80)

penup()
goto(150, 100)
pendown()

left(90)
forward(30)

left(90)
forward(80)

#step 11: drawing the king

color("sienna")

penup()
goto(0, 10)
pendown()



















exitonclick()