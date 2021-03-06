#########################################
#### Rainbow Target Coding Challenge ####
#### By Sarah Ahmed #####################
#### March 16th, 2020 ###################
#########################################

from tkinter import*
from random import*
from math import*
from time import*
myInterface = Tk()
screen = Canvas( myInterface, width=700, height=700, background="black" )
screen.pack()


##################
##### TARGET #####
##################
screen.create_oval(351,351, 350,350, fill = "white", outline = "white", width = 3)

for n in range(7):
    d = 60*n
    x1target = 350 - d
    x2target = 350 + d
    y1target = 350 - d
    y2target = 350 + d

    screen.create_oval(x1target,y1target, x2target,y2target, outline = "white")

##########################
##### BALL ANIMATION #####
##########################:
xball = randint(0,700)
yball = randint(0,700)
xxball = xball + 30
yyball = yball + 30
xspeed = 5
yspeed = 2


colour = "hot pink"
while True:
    ball = screen.create_oval(xball,yball, xxball,yyball, fill = colour)
        
    screen.update()
    sleep(0.03)
    screen.delete(ball)

    xball = xball + xspeed
    yball = yball + yspeed
    xxball = xball + 30
    yyball = yball + 30

    #perimeter restrictions
    if xxball >= 700:
        xspeed = xspeed * -1

    elif xball <= 0:
        xspeed = xspeed * -1

    if yyball >= 700:
        yspeed = yspeed * -1

    if yball <= 0 :
        yspeed = yspeed * -1

    #measuring distance from centre to change colours accordingly
    #centre of ball (a,b)
    a = (xball + xxball)/2
    b = (yball + yyball)/2

    distance = sqrt((350 - a)**2 + (350 - b)**2)

    if distance < 60:
        colour = "red"
    elif 60 < distance < 120:
        colour = "orange"
    elif 120 < distance < 180:
        colour = "yellow"
    elif 180 < distance < 240:
        colour = "green"
    elif 240 < distance < 300:
        colour = "blue"
    elif 300 < distance < 360:
        colour = "purple"
    else:
        colour = "hot pink"
