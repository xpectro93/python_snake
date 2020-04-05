import turtle


wn = turtle.Screen()
wn.title("Snake Test")
wn.bgcolor('black')

wn.setup(width=1000, height=1000)

pen = turtle.Pen()
for y in range(-500,500,10):
    pen.color('white')
    pen.goto(y,y)
    pen.speed(0)
    print(y)



while True:
    wn.update()