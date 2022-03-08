from turtle import Turtle

class ScoreBoard:
    """A class to create scoreboard to keep track of players score
    
    Attributes: score --> object of scoreboard turtle on screen
    
    Methods: display(self, count) --> to display score of players on screen

             game_over(self, text) --> to display game over text on screen when one of the player loses"""
    
    def __init__(self, pos):
        scoreboard = Turtle()
        scoreboard.penup()
        scoreboard.hideturtle()
        scoreboard.color("white")
        scoreboard.goto(pos)
        self.score = scoreboard

        self.display(count=0)

    def display(self,count):
        self.score.write(arg= f"{count}", align='center', font=("ribbon", 30, "bold"))

    def game_over(self, text):
        self.score.goto(0,0)
        self.score.write(arg= f"{text}", align='center', font=("arial", 30, "bold"))