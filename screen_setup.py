from turtle import Screen, Turtle

WIDTH = 800
HEIGHT = 600

class ScreenSetup:
    """Class to initialize screen
    
    Attribute: screen -- > holds Screen object"""
    
    def __init__(self):
        #Screen Setting
        screen = Screen()
        screen.setup(width=WIDTH, height=HEIGHT)
        screen.bgcolor("black")
        screen.tracer(0)
        screen.title("Pong Game")
        self.screen = screen
        
        #center Line setting
        turtle = Turtle()
        turtle.hideturtle()
        turtle.color("white")
        turtle.penup()
        turtle.goto(0, -300)
        turtle.pendown()
        turtle.setheading(90)
        for _ in range(8):
            turtle.forward(40)
            turtle.penup()
            turtle.forward(40)
            turtle.pendown()
