from turtle import left, forward, exitonclick

uhel= int(input('Kolik chceš úhlů?'))

for i in range(uhel):
    forward(50)
    left(360/uhel)
exitonclick ()
