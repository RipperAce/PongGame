from turtle import Turtle
import time

class PongBall:
    """A Class to create a pong ball on screen.
    
    Attributes: ball --> object of pong ball on screen
    
    Methods: move(self, move_dir, direction1, direction2, right_paddle, left_paddle) --> a method to move and bounce pong from top, bottom as well as paddles
    
             count_score(self) --> Method to reset pong ball to center when it goes out of screen."""
    
    def __init__(self):
        ball = Turtle(shape="circle")
        ball.penup()
        ball.color("white")

        self.ball = ball

    def move(self, move_dir, direction1, direction2, rp, lp):
        idx1 = direction1.index(move_dir)
        new_idx1 = (idx1+2)%len(direction1)

        idx2 = direction2.index(move_dir)
        new_idx2 = (idx2+2)%len(direction2)

        if self.ball.ycor() < -270 or self.ball.ycor() > 280:
            self.ball.setheading(direction1[new_idx1])
            move_dir = direction1[new_idx1]
            self.ball.forward(20)
            return move_dir
        elif self.ball.distance(rp) < 50 and 360 > self.ball.xcor() > 350 and move_dir in direction2[0:2]:
            self.ball.setheading(direction2[new_idx2])
            move_dir = direction2[new_idx2]
            self.ball.forward(20)
            return move_dir
        elif self.ball.distance(lp) < 50 and -370 < self.ball.xcor() < -360 and move_dir in direction2[2:4]:
            self.ball.setheading(direction2[new_idx2])
            move_dir = direction2[new_idx2]
            self.ball.forward(20)
            return move_dir
        else:
            self.ball.setheading(move_dir)
            self.ball.forward(20)
            return move_dir

    def count_score(self):
        if self.ball.xcor() > 390:
            time.sleep(0.2)
            self.ball.goto(0, 0)
            return False
        elif self.ball.xcor() < -390:
            time.sleep(0.2)
            self.ball.goto(0, 0)
            return True