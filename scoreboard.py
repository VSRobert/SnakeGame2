from turtle import Turtle

import asyncio

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read()) #deoarece il citeste ca string si noi il vom folosi ca si numar (int)
        self.goto(0, 270)   #pentru a il pozitiona in top-centru
        self.color("white")  #pentru ca default scrie negru si am modificat sa fie alb
        self.hideturtle()  #pentru a disparea pin-ul cu sageata/turtle
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align="center",font=("Arial", 12, "normal"))  # functie de text din turtle module

    def increase_score(self):
        self.score +=1

        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data: #suprascriem data.txt cand avem un nou high_score
                data.write(f"{self.high_score}")  #il suprascriem ca string ca oricum il convertim ca integer cand il citim
        self.score = 0 #pentru a reseta scorul
        self.update_scoreboard()
    #def game_over(self):
     #   self.goto(0,0)
      #  self.write("GAME OVER", align="center", font=("Arial", 35, "normal"))

