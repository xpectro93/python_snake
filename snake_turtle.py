import turtle


wn = turtle.Screen()
wn.title("Snake Test")
wn.bgcolor('black')

wn.setup(width=1000, height=1000)

for x in range(0, 100):
    pen = turtle.Turtle()
    pen.color('white')
    pen.speed(6)
    pen.goto(0,x)
    pen.forward(1000)

while True:
    wn.update()