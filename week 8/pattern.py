import turtle as t
from random import randint
def setup():
  t.clearscreen()
  t.screensize(1000, 800)
  t.speed(100)

def randcolor():
  num = randint(1,4)
  if num == 1:
    t.color("red")
  elif num == 2:
    t.color("blue")
  elif num == 3:
    t.color("green")
  else:
    t.color == ("orange")

def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
  t.up()
  t.goto(centerX, centerY)
  t.seth(0)
  num = 360/count
  for i in range(0, count):
    randcolor()
    t.fd(offset)
    t.down()
    for j in range(0, 2):
      t.fd(width)
      t.rt(90)
      t.fd(height)
      t.rt(90)
    t.up()
    t.goto(centerX, centerY)
    t.lt(num)

def drawCirclePattern(centerX, centerY, offset, radius, count):
  t.up()
  t.goto(centerX, centerY)
  t.seth(0)
  num = 360/count
  for i in range(0, count):
    randcolor()
    t.fd(offset)
    t.down()
    t.circle(radius)
    t.up()
    t.goto(centerX, centerY)
    t.lt(num)


def drawSuperPattern(num = randint(1, 10)):
  for i in range(0, num):
    if randint(1,2) == 1:
      drawRectanglePattern(randint(1, 200), randint(1, 160), randint(1, 100), randint(1, 50), randint(1, 50), randint(5, 100), randint(1, 360))
    else:
      drawCirclePattern(randint(1, 200), randint(1, 160), randint(1, 100), randint(1, 100), randint(5, 100))

def done():
  t.clear()