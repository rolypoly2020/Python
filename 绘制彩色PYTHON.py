import turtle
c1=['red','blue','green','brown','purple','black']
str1='python'
for i in range(6):
    turtle.pencolor(c1[i])
    turtle.write(str1[i],font=("3ds",96,'bold'))
    turtle.penup()
    turtle.fd(65)
    turtle.pendown()
turtle.hideturtle()
turtle.done()