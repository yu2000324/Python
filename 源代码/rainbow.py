import turtle
size = 15
turtle.pensize(15)
for i in range(7):
    if i == 0:
        turtle.color('purple')
    if i == 1:
        turtle.color('blue')
    if i == 2:
        turtle.color('cyan')
    if i == 3:
        turtle.color('green')
    if i == 4:
        turtle.color('yellow')
    if i == 5:
        turtle.color('orange')
    if i == 6:
        turtle.color('red')
    turtle.circle(size)
    size += 15
    if i == 6:
        break
    turtle.seth(-90)
    turtle.penup()
    turtle.fd(15)
    turtle.pendown()
    turtle.seth(360)
turtle.fd(-3)
turtle.seth(-90)
turtle.color('purple')
turtle.pensize(17)
turtle.fd(200)
turtle.done()
