import turtle
import pandas as pd
screen =  turtle.Screen()
screen.title("Guess The States")
image = "india_outline.gif"
screen.register_shape(image)
turtle.shape(image)

def clicker(x,y):
    print(x,y)

screen.onscreenclick(clicker)
turtle.mainloop()