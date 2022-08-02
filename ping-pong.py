import turtle

wind = turtle.Screen()
wind.title("ping pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()  # clean line
ball.goto(0, 0)  # posion in screen
ball.dx = 0.5
ball.dy = 0.5

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)

# madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("yellow")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()  # clean line
madrab1.goto(-350, 0)  # posion in screen

# madrab2

madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("blue")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()  # clean line
madrab2.goto(350, 0)  # posion in screen




# function

def madrab1_up():
    y = madrab1.ycor()
    y += 30
    madrab1.sety(y)

def madrab1_down():
     y = madrab1.ycor()
     y -= 30
     madrab1.sety(y)

     # madrab postion

    # keyboard bindings

wind.listen()
wind.onkeypress(madrab1_up, "1")
wind.onkeypress(madrab1_down, "2")

def madrab2_up():
    y = madrab2.ycor()
    y += 30
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y -= 30
    madrab2.sety(y)
 # control arm

# madrab1.breakpoint(-350, 250)
# madrab1.breakpoint(-350, -250)

# madrab2.breakpoint(350, 250)
# madrab2.breakpoint(350, -250)


    # keyboard bindings

wind.listen()
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")


while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
       ball.setx(390)
       ball.dx *= -1

       score1 += 1
       score.clear()
       score.write("player1 = {}, player2 = {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1



    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40) and (
           ball.ycor() > madrab2.ycor() - 40):
       ball.setx(340)
       ball.dx *= -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40) and (
            ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        score2 += 1
        score.color()
        score.write("player1 = {}, player2 = {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

        # moving madrab 1 and madrab 2

    if madrab1.ycor() >= 295:
       madrab1.sety(295)

    if madrab1.ycor() <= -295:
       madrab1.sety(-295)

    if madrab2.ycor() <= -295:
       madrab2.sety(-295)

    if madrab2.ycor() >= 295:
       madrab2.sety(295)
