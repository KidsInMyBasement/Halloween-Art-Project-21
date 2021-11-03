import turtle
import random as rand
score = 0
#-----game configuration----
"""def score():"""
# shape = "turtle"
color = "purple"
size = 4
tr = turtle.Turtle()
wn = turtle.Screen()
wn.addshape('bg2.gif')
wn.bgcolor("black")
wn.addshape('ghost.gif')
# x = tr.shape('ghost.gif')
#-----initialize turtle-----
t = turtle.Turtle()
t.shape('ghost.gif')
t.fillcolor(color)
t.shapesize(size)
#-----game functions--------
def change_position():
  rand.randint(-200,200)
  rand.randint(-150,150)
  new_x_pos = rand.randint(-200,200)
  new_y_pos = rand.randint(-150,150)
  t.penup()
  t.goto(new_x_pos,new_y_pos)

def squaro_clicked(x,y):
  change_position()
  
#-----events----------------
t.onclick(squaro_clicked)
wn = turtle.Screen()
wn.mainloop()