#海龟绘图-五环
import turtle

#设置画笔宽度
turtle.width(10)

turtle.color('red')
turtle.circle(50)


turtle.penup() #画笔弹起
turtle.goto(120,0)
turtle.pendown() #画笔按下

turtle.color('blue')
turtle.circle(50)

turtle.penup()
turtle.goto(240,0)
turtle.pendown()

turtle.color('yellow')
turtle.circle(50)

turtle.penup()
turtle.goto(60,-50)
turtle.pendown()

turtle.color('black')
turtle.circle(50)

turtle.penup()
turtle.goto(180,-50)
turtle.pendown()

turtle.color('green')
turtle.circle(50)

