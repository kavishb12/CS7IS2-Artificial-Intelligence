#coding: utf-8

from turtle import *

ht()

# Let's have some fun, hehe.

def show_board(solution, locked, score, pos=(-225, -225), size=50,
               turtle=getturtle()):
               
    screen = Screen()
    screen.setup(width=size*10, height=size*10)
    
    # background color: green == solved, red == not solved
    if score == 0:
        screen.bgcolor("green")
    else:
        screen.bgcolor("red")
    
    # Display score in title
    screen.title("Score: %s" % str(score))
    
    # some turtle preferences
    screen.mode("logo")
    screen.tracer(8, 25)
    turtle.ht()
    turtle.pu()
    turtle.speed(0)
    turtle.setpos(pos)
    turtle.pd()
    turtle.color("black", "white")
    
    def square(s, turtle=turtle):
        """Draws a square."""
        turtle.seth(0)
        turtle.pensize(3)
        for i in range(4):
            turtle.fd(s)
            turtle.rt(90)
    turtle.begin_fill()
    square(size * 9, turtle)
    turtle.end_fill()
    
    def lines(s):
        turtle.seth(90)
        for i in range(1, 9):
            if i in [3, 6]:
                turtle.pensize(2)
            else:
                turtle.pensize(1)
            turtle.pu()
            turtle.setpos(pos[0], pos[1] + s*i)
            turtle.pd()
            turtle.fd(s * 9)

        turtle.seth(0)
        for i in range(1, 9):
            if i in [3, 6]:
                turtle.pensize(2)
            else:
                turtle.pensize(1)
            turtle.pu()
            turtle.setpos(pos[0] + s*i, pos[1])
            turtle.pd()
            turtle.fd(s * 9)
            
    lines(size)
    
    def numbers(solution, pos, locked, s=size):
        tuples = []
        for y in range(9, 0, -1):
            for x in range(1, 10):
                tuples.append((x, y))
        for dt in tuples:
            hideturtle()
            pu()
            seth(0)
            setpos((pos[0]+s/2.0*(2*dt[0]-1), pos[1]+s/2.0*(2*dt[1]-1.4)))
            index = tuples.index(dt)
            try:
                z = solution[index][0]
            except:
                z = solution[index]
            if index in locked:
                spec = "bold"
                pencolor("black")
            else:
                spec = "normal"
                pencolor("dark green")
            write(z, False, "center", font=("Arial", 14, spec))

    numbers(solution, pos, locked, size)
    screen.update()
    return (screen, turtle.getturtle())
