from random import *
from fractions import Fraction
count = 0
total = 0

while False:
    x, y = random(), random()
    
    if x*x + y*y < 1:
        count+=1
    total+=1
    pi = 4*float(count/total)
    if total%100000 == 0:
        print(total, pi)

leibniz = 1
i = 1
while False:
    leibniz+=(-1)**(i)*float(1/(2*i+1))
    i+=1

    if i%100000000 == 0:  
        print(leibniz*4)