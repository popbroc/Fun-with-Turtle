

import turtle
import random
wn = turtle.Screen()
name = "Ian"
wn.bgcolor("lightblue")
queen=turtle.Turtle()
queen.speed(20)
x = 0


queen.pendown() 
while x < 12:
  
    queen.forward(10)     
    queen.right(30)
    queen.forward(10)
    queen.right(30)
    queen.forward(10)
    queen.right(30)
    queen.forward(10)
    queen.right(30)
    queen.forward(10)
    queen.right(30)
    queen.forward(10)
    queen.right(30)

    queen.right(20) 
    x = x+1 # adds 1 to the value of x,
wn.exitonclick()
