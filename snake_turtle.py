import turtle


wn = turtle.Screen()
wn.title("Snake Test")
wn.bgcolor('black')

wn.setup(width=1000, height=1000)

for x in range(0, 500):
    pen = turtle.Turtle()
    if x % 10 == 0:
        pen.color('blue')
        pen.speed(0)
        pen.goto(x,x)
        pen.forward(1000)
    else:
        pen.color('red')
        pen.speed(0)
        pen.goto(-x,-x)
        pen.forward(1000)


while True:
    wn.update()