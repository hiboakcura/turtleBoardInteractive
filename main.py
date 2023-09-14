import turtle

drawing_board= turtle.Screen()
drawing_board.bgcolor("purple")
drawing_board.title("drawing board")

turtle_instance= turtle.Turtle()

def tforward():
    turtle_instance.forward(100)

def trotright():
    turtle_instance.right(10)

def trotleft():
    turtle_instance.left(10)

def clearSecren():
    turtle_instance.clear()

def thome():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

def tpenup():
    turtle_instance.penup()

def tpedown():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(fun=tforward, key="space")
drawing_board.onkey(fun=trotright, key="Down")
drawing_board.onkey(fun=trotleft, key="Up")
drawing_board.onkey(fun=clearSecren, key="c")
drawing_board.onkey(fun=thome, key="h")
drawing_board.onkey(fun=tpenup, key="q")
drawing_board.onkey(fun=tpedown, key="w")

turtle.mainloop()