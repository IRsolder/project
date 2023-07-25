import turtle as t

win = t.Screen()
win.title("بازی پینگ پونگ")
win.setup(height=600,width=800)
win.bgcolor('green4')
win.tracer(0)

dayere3= t.Turtle()
dayere3.speed(0)
dayere3.shape("circle")
dayere3.color('white')
dayere3.penup()
dayere3.goto(370,270)
dayere3.forward(0)
dayere3.shapesize(5)


dayere4= t.Turtle()
dayere4.speed(0)
dayere4.shape("circle")
dayere4.color('green4')
dayere4.penup()
dayere4.goto(370,270)
dayere4.forward(0)
dayere4.shapesize(3)



dayere3= t.Turtle()
dayere3.speed(0)
dayere3.shape("circle")
dayere3.color('white')
dayere3.penup()
dayere3.goto(-370,270)
dayere3.forward(0)
dayere3.shapesize(5)

dayere5= t.Turtle()
dayere5.speed(0)
dayere5.shape("circle")
dayere5.color('green')
dayere5.penup()
dayere5.goto(-370,270)
dayere5.forward(0)
dayere5.shapesize(3)

dayere6= t.Turtle()
dayere6.shape("circle")
dayere6.color('white')
dayere6.penup()
dayere6.goto(370,-270)
dayere6.forward(0)
dayere6.shapesize(5)

dayere7= t.Turtle()
dayere7.speed(0)
dayere7.shape("circle")
dayere7.color('green')
dayere7.penup()
dayere7.goto(370,-270)
dayere7.forward(0)
dayere7.shapesize(3)

dayere8= t.Turtle()
dayere8.shape("circle")
dayere8.color('white')
dayere8.penup()
dayere8.goto(-370,-270)
dayere8.forward(0)
dayere8.shapesize(5)

dayere9= t.Turtle()
dayere9.speed(0)
dayere9.shape("circle")
dayere9.color('green')
dayere9.penup()
dayere9.goto(-370,-270)
dayere9.forward(0)
dayere9.shapesize(3)

dayere= t.Turtle()
dayere.speed(0)
dayere.shape("circle")
dayere.color('white')
dayere.penup()
dayere.goto(0,0)
dayere.forward(0)
dayere.shapesize(15)

dayere= t.Turtle()
dayere.speed(0)
dayere.shape("circle")
dayere.color('green4')
dayere.penup()
dayere.goto(0,0)
dayere.forward(0)
dayere.shapesize(13)

khat= t.Turtle()
khat.speed(0)
khat.shape("square")
khat.color('white')
khat.penup()
khat.goto(0,0)
khat.shapesize(stretch_wid=35,stretch_len=1)

khat2= t.Turtle()
khat2.speed(0)
khat2.shape("square")
khat2.color('white')
khat2.penup()
khat2.goto(385,0)
khat2.shapesize(stretch_wid=35,stretch_len=1)

khat3= t.Turtle()
khat3.speed(0)
khat3.shape("square")
khat3.color('white')
khat3.penup()
khat3.goto(-390,0)
khat3.shapesize(stretch_wid=35,stretch_len=1)

khat4= t.Turtle()
khat4.speed(0)
khat4.shape("square")
khat4.color('white')
khat4.penup()
khat4.goto(0,290)
khat4.shapesize(stretch_wid=1,stretch_len=40)

khat5= t.Turtle()
khat5.speed(0)
khat5.shape("square")
khat5.color('white')
khat5.penup()
khat5.goto(0,-290)
khat5.shapesize(stretch_wid=1,stretch_len=40)

pad_a= t.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color('blue')
pad_a.penup()
pad_a.goto(-350,0)
pad_a.shapesize(stretch_wid=5,stretch_len=1)
pad_a_amtyaz= 0

pad_b= t.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color('red')
pad_b.penup()
pad_b.goto(350,0)
pad_b.shapesize(stretch_wid=5,stretch_len=1)
pad_b_amtyaz= 0

ball1= t.Turtle()
ball1.shape("circle")
ball1.color('black')
ball1.goto(0,0)
ball1.shapesize(0.5)

ball= t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 0.5
ball_dy = 0.5
ball.shapesize(1.5)


#pen
pen= t.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.goto(0,240)
pen.hideturtle()
pen.write(f" پرسپولیس :{pad_a_amtyaz}         استقلال:  {pad_b_amtyaz}", align="center", font=("homa", 15))




def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)
#bind

win.listen()
win.onkeyrelease(pad_a_up,"q")
win.onkeyrelease(pad_a_down,"a")
win.onkeyrelease(pad_b_up,"Up")
win.onkeyrelease(pad_b_down,"Down")
while True:
    win.update()

    ball.sety(ball.ycor() + ball_dy)
    ball.setx(ball.xcor() + ball_dx)

    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball_dy *= -1

    if ball.xcor() > 400:
        ball.goto(0,0)
        ball_dx *= -1
        pen.clear()
        pad_b_amtyaz += 1
        pen.write(f"پرسپولیس :{pad_a_amtyaz}        استقلال:{pad_b_amtyaz}", align="center", font=("homa", 15))
    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball_dx *= -1
        pen.clear()
        pad_a_amtyaz += 1
        pen.write(f"پرسپولیس :{pad_a_amtyaz}           استقلال:{pad_b_amtyaz}", align="center", font=("homa", 15))

    if ((ball.xcor() > 330 and ball.xcor() < 331) and (ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50)):
        ball.setx(330)
        ball_dx *= -1
    if ((ball.xcor() < -330 and ball.xcor() > -331) and (ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50)):
        ball.setx(-330)
        ball_dx *= -1