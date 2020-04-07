import turtle
import random

# wn = turtle.Screen()
# wn.title("Snake Test")
# wn.bgcolor('black')

# wn.setup(width=1000, height=1000)

# pen = turtle.Turtle()
# pen.penup()
# pen.goto(0,400)
# pen.pensize(5)
# pen.speed(5)
# pen.color('red')
# pen.pendown()
# pen.goto(175,-75)
# pen.goto(-250,250)
# pen.goto(250,250)
# pen.goto(-175,-75)
# pen.goto(0,400)
# pen.speed(7)
# pen.penup()
# pen.goto(0,375)
# pen.pendown()
# pen.circle(-238)


# pen.speed(0)
# pen.penup()
# pen.goto(0,-375)
# pen.pendown()
# pen.write("Made by: Don Jon", align='center', font=('Courier', 24, "normal") )
loadWindow = turtle.Screen()
loadWindow.setup(width=1000, height=1000)
loadWindow.bgcolor("black")
turtle.speed(0)
turtle.colormode(255)
turtle.pensize(3)

def draw_grid(STEP,LENGTH):
    for i in range(-500, LENGTH, STEP):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        turtle.pencolor(r,g,b)
        #Start -490, 500
        # 
        #changed  i top to bottom lines(horizontal)
        turtle.penup()
        turtle.setpos(-500, LENGTH/2)
        turtle.pendown()
        turtle.setpos(-LENGTH/2 + i, -LENGTH/2)


        turtle.penup()
        turtle.setpos(LENGTH/2, -500)
        turtle.pendown()
        turtle.setpos(-500, -LENGTH/2 + i)

    
draw_grid(25,1000)
while True:
    loadWindow.update()