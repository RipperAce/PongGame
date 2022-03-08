from turtle import Turtle

STRETCH_WID = 5
STRETCH_HGT = 1

class Paddle:
    """A Class tocreate left and right paddles.
    
    Attributes: paddle --> Paddle object
    
    Methods: init_pos(self, x_pos, y_pos) --> Initializes paddle on screen at x and y positions

             up(self) --> Moves paddle upside by 20 steps
    
             down(self) --> Moves paddle downside by 20 steps"""
    
    def __init__(self, x_pos, y_pos):
        paddle = Turtle(shape="square")
        paddle.shapesize(stretch_len=STRETCH_HGT, stretch_wid=STRETCH_WID)
        paddle.color("white")
        paddle.penup()
        paddle.speed("fast")
        
        self.paddle = paddle
        self.init_pos(x_pos, y_pos)

    def init_pos(self, x_pos, y_pos):
        self.paddle.goto((x_pos, y_pos))

    def up(self):
        if self.paddle.ycor() < 250:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def down(self):
        if self.paddle.ycor() > -240:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)