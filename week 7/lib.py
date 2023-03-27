import turtle as t

def drawChessboard(startX, startY, width=250, height=250):
  t.up()
  t.goto(startX, startY)
  t.down()
  s_width = width/8
  s_height = height/8
  t.color("black")
  for h in range(0,4):
    for j in range(0, 4):
      t.begin_fill()
      for i in range(0,2):
        t.fd(s_width)
        t.lt(90)
        t.fd(s_height)
        t.lt(90)
      t.end_fill()
      t.up()
      t.fd(2*s_width)
      t.down()
    t.lt(90)
    t.fd(s_height)
    t.lt(90)
    for i in range(0,4):
      t.begin_fill()
      for j in range(0,2):
        t.fd(s_width)
        t.rt(90)
        t.fd(s_height)
        t.rt(90)
      t.end_fill()
      t.up()
      t.fd(2*s_width)
      t.down()
    t.rt(90)
    t.fd(s_height)
    t.rt(90)
  t.color("red")
  for i in range(0, 2):
    t.fd(width)
    t.rt(90)
    t.fd(height)
    t.rt(90)
