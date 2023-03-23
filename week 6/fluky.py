import time
from random import seed
from random import randint
fluky = 0
num = []
st = time.time()
for i in range(2, 10000):
  for j in range(1, i):
    if i % j == 0:
      seed(j)
      fluky += randint(1, i)
  if i == fluky:
    num.append(i)
  fluky = 0
et = time.time()
print(num)
print(et-st)