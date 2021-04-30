import pygame as py
import time
py.init()
screen = py.display.set_mode((500,500))
py.display.set_caption("My First Game")
running = True
x,y = 50,50
dx=1
dy=1
speed = 5
r = 50

clock = py.time.Clock()
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    if x==480:
        dx=-2
    elif x==0:
        dx=1
    if y ==480:
        dy=-1
    elif y==0:
        dy*=-1
        
    x=x+5*dx
    y=y+5*dy
    py.draw.circle(screen, (0,255,0), (x,y), 20, 18)
    py.display.flip()
    screen.fill((0,0,0))
    clock.tick(60)

py.quit()