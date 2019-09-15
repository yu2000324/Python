import turtle
turtle.title("自动轨迹绘制")
turtle.setup(800, 600, 0, 0)
turtle.pencolor("red")
turtle.pensize(5)
datals = []
f = open("date.txt", "r", encoding="utf-8")
for line in f:
    line = line.replace("\n", "")
    datals.append(list(map(eval, line.split(","))))
f.close()
for i in range(len(datals)):
    turtle.pencolor(datals[i][3], datals[i][4], datals[i][5])
    turtle.fd(datals[i][0])
    if datals[i][1]:
        turtle.right(datals[i][2])
    else:
        turtle.left(datals[i][2])
turtle.hideturtle()
turtle.done()
