# Turtle Party Project
# by Shaun Washington
# 03.11.24

import turtle
turtle.color("blue")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
#forward helper function
def move(len):
  back(-1 * len)

def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)

def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(75, 45)
move(150)
turtle.color("red")
spiral(100, 90)

#def square(size):
  #for i in range(4):
    #turtle.forward(size)
    #turtle.left(90)

#for n in range(3, 10):
  #move(50) # forward
  #polygon(n, 100 / n)
  #back(50)
  #turtle.right(360 / 7)

#triangle(100)
#back(25)
#triangle(50)
#back(25)
#triangle(25)
