import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.hideturtle()
t.goto(0,-10)
t.pensize(3)
t.color('turquoise')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()
t.penup()
t.goto(-75,130)
t.pendown()
t.color('white')
t.penup()
t.goto(-80,130)
t.pendown()
t.color('black')
t.write("Eu te amo",font=("Verdana",20,"bold"))
turtle.done()
