import turtle

wind = turtle.Screen()
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)
wind.title("Ping Pong")

# objects

# player1
p1 = turtle.Turtle()
p1.color("blue")
p1.shape("square")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(350, 0)
p1.cnt = 0

# player2
p2 = turtle.Turtle()
p2.color("red")
p2.shape("square")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(-350, 0)
p2.cnt = 0

# ball
b = turtle.Turtle()
b.color("white")
b.shape("circle")
b.penup()
b.goto(0, 0)
b.dx = .2
b.dy = -.12

# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1 : " + str(p1.cnt) + " VS Player 2 : " + str(p2.cnt), align="center",
            font=("courier", 24, "normal"))
score.shapesize(stretch_wid=2, stretch_len=1)


# player one Movement
def p1_up():
    if 260 > p1.ycor() >= -240:
        y = p1.ycor()
        y += 20
        p1.sety(y)


def p1_down():
    if 260 >= p1.ycor() > -240:
        y = p1.ycor()
        y -= 20
        p1.sety(y)


# player two Movement

def p2_up():
    if 260 > p2.ycor() >= -240:
        y = p2.ycor()
        y += 20
        p2.sety(y)


def p2_down():
    if 260 >= p2.ycor() > -240:
        y = p2.ycor()
        y -= 20
        p2.sety(y)


# keyboard blinding
wind.listen()
wind.onkeypress(p1_up, 'Up')
wind.onkeypress(p1_down, 'Down')
wind.onkeypress(p2_up, 'w')
wind.onkeypress(p2_down, 's')
while True:
    wind.update()
    b.sety(b.ycor() + b.dy)
    b.setx(b.xcor() + b.dx)

    if b.ycor() >= 290:
        b.sety(290)
        b.dy *= -1
    if b.ycor() < -290:
        b.sety(-290)
        b.dy *= -1
    if b.xcor() >= 390:
        b.goto(0, 0)
        b.dx *= -1
        p2.cnt += 1
        score.clear()
        score.write("Player 1 : " + str(p1.cnt) + " VS Player 2 : " + str(p2.cnt), align="center",
                    font=("courier", 24, "normal"))
    if b.xcor() <= -390:
        b.goto(0, 0)
        b.dx *= -1
        p1.cnt += 1
        score.clear()
        score.write("Player 1 : " + str(p1.cnt) + " VS Player 2 : " + str(p2.cnt), align="center",
                    font=("courier", 24, "normal"))

    if b.xcor() > 340 and (p1.ycor() + 40) > b.ycor() > (p1.ycor() - 40):
        b.setx(340)
        b.dx *= -1
    if b.xcor() < -340 and (p2.ycor() + 40) > b.ycor() > (p2.ycor() - 40):
        b.setx(-340)
        b.dx *= -1
