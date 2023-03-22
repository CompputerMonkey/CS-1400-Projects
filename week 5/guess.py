import random as r
if input("guess a number between 1 and 10: ") == r.randint(1,10):
  print("you got it correct!")
else:
  print("just give up")