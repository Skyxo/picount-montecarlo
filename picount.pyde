from random import *
from fractions import Fraction
from decimal import Decimal

circlecount = 0
total = 0

def setup():
    size(510,510)
    background(0,0,0)
    stroke(255)
    noFill()

    rect(5,5,250*2,250*2)
    circle(255,255,250*2)
    
def draw():
    global circlecount, total
    translate(width/2, height/2)
    
    for i in range(10000):
        x, y = uniform(-1,1), uniform(-1,1)
            
        if x*x + y*y <= 1:
            circlecount += 1
            stroke(255,0,255)
        else:
            stroke(255,255,0)
        total += 1

        point(x*250, y*250)
    
    #pi = float(4)*Fraction(circlecount, total)
    #pi = 4*Decimal(circlecount)/Decimal(total)
    #print((circlecount, total), float(circlecount)/float(total), Decimal(circlecount)/Decimal(total), Fraction(circlecount, total))
    print(total, float(4)*Fraction(circlecount, total))
    print(total, Decimal(4)*Decimal(circlecount)/Decimal(total))
