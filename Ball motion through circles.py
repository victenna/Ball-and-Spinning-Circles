import turtle,random,time
wn=turtle.Screen()
wn.setup(900,700)
wn.bgcolor('red')
wn.tracer(2)
R=200
delta=20
back=-10
dx=10
t=[]
for m in range(3):
    t.append(turtle.Turtle())
    t[m].hideturtle()
    t[m].pensize(2)
    t[m].up()
    t[m].goto(0,-R/2*(m+1))
    t[m].down()
    t[m].color('blue')
    t[m].circle(R/2*(m+1))
k=[]
for i in range(3):
    k.append(turtle.Turtle())
    k[i].shape('square')
    k[i].shapesize(1,3)
    k[i].hideturtle()
    k[i].color('red')
    k[i].up()
    k[i].goto(0,-R*(i+1)/2)
    k[i].circle(R*(i+1)/2,i*90)
    k[i].showturtle()
wn.tracer(2)
text=[]

for i in range(4):
    text.append(turtle.Turtle())
    text[i].hideturtle()
    text[i].up()

def ttext(i,X,Y,message):
    text[i].goto(X,Y)
    text[i].down()
    text[i].color('white')
    text[i].write(message,font=('Time Romain',20,'bold'))

ttext(0,-400,300,'TAP LEFT ARROW KEY to move the ball through the circles')
ttext(1,-440,-50,'START')
ttext(2,310,-50,'FINISH')

ball=turtle.Turtle('circle')
ball.up()
ball.goto(-400,0)

ball.color('gold')
ball.setheading(0)
ball.shapesize(1)
while True:
    k[0].circle(R/2,5)
    k[1].circle(R,5)
    k[2].circle(3*R/2,5)
    time.sleep(0.03)

    if ball.xcor()>-(R/2+delta) and ball.xcor()<-R/2 and k[0].xcor()>-(R/2-delta/4):
        ball.fd(back)
    if ball.xcor()>(R/2-delta) and ball.xcor()<R/2 and k[0].xcor()<=(R/2-delta/4):
        ball.fd(back)

    if ball.xcor()>-(R+delta) and ball.xcor()<-R and k[1].xcor()>-(R-delta/4):
        ball.fd(back)
    if ball.xcor()>(R-delta) and ball.xcor()<R and k[1].xcor()<=(R-delta/4):
        ball.fd(back)

    if ball.xcor()>-(3*R/2+delta) and ball.xcor()<-3*R/2 and k[2].xcor()>-(3*R/2-delta/4):
        ball.fd(back)
    if ball.xcor()>(3*R/2-delta) and ball.xcor()<3*R/2 and k[2].xcor()<=(3*R/2-delta/4):
        ball.fd(back)
    def move_right():
        ball.setheading(00)
        ball.fd(dx)
        if ball.xcor()>3*R/2:
            ttext(3,240,0,'GAME OVER')
            time.sleep(2)
            text[3].clear()
            ball.goto(-400,0)
    def move_left():
        ball.setheading(180)
        ball.fd(dx)
    wn.onkey(move_right,'Right')
    wn.onkey(move_left,'Left')
    wn.listen()
    

    

