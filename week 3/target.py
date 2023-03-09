import turtle as t

xPos = int(input("enter the x of the bullseye : \n"))
yPos = int(input("enter the y of the bullseye : \n"))

ratio = 2

t.goto(xPos, yPos-(23*ratio))
t.color("black")
t.begin_fill()
t.circle(27*ratio)
t.end_fill()


t.goto(xPos, yPos-(ratio*13))
t.color("cyan")
t.begin_fill()
t.circle(ratio*17)
t.end_fill()


t.goto(xPos, yPos-(ratio*6))
t.color("red")
t.begin_fill()
t.circle(ratio*10)
t.end_fill()



t.goto(xPos, yPos)
t.color("yellow")
t.begin_fill()
t.circle(ratio*4)
t.end_fill()