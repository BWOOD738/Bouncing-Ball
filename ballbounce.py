import turtle

global wn
wn = turtle.Screen()

global S_WIDTH
global S_HEIGHT

S_WIDTH = 800
S_HEIGHT = 600

class Win:
 
 def Window():
  wn.setup(S_WIDTH, S_HEIGHT)
  wn.bgcolor("black")
  wn.title("Ball bounce")
 Window()

Win()

class Ball:

 def ballProperties():
  global ball
  balls = []

  ball = turtle.Turtle()
  ball.shape("circle")
  ball.color("green")
  ball.penup()
  ball.speed()
  ball.goto(0, 200)
  ball.dy = -2
  ball.dx = 2

 ballProperties()

 global gravity
 gravity = 0.1
 
Ball()



while True:
    wn.update()

    ball.dy -= gravity

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #check for bounce 
    if ball.ycor() < -S_HEIGHT + 300:
        ball.dy *= -1
    # check for wall collision
    if ball.xcor() > 375:
        ball.dx *= -1
    if ball.xcor() < -375:
        ball.dx *= -1
    

wn.mainloop()