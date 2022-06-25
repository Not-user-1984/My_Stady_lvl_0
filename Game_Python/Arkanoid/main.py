import pgzero
import pgzrun


TITLE = "Arkanoid_clon"
WIDTH = 800
HEIGHT = 500
pgzrun.go()

paddle = 'Actor'("paddleblue.png")
paddle.x = 120
paddle.y = 420


ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300

def draw():
    paddle.draw()
    ball.draw()

def update():
    pass
