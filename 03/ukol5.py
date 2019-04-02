from turtle import shape, left, right, forward
from math import sqrt
from turtle import exitonclick


shape("turtle")
left(180)
forward(300)
left(180)
forward(100)

for i in range(4):
    left(135)
    forward(sqrt(2)*100)
    right(135)
    forward(100)
    left(135)
    forward(sqrt(2)*100/2)
    left(90)
    forward(sqrt(2)*100/2)
    left(45)
    forward(100)
    left(135)
    forward(sqrt(2)*100)
    right(135)
    forward(100)
    left(90)
    forward(125)


exitonclick()