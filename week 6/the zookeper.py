import random as r
import fraction as f
r.seed(r.randint(1,100000))
check = 0
el1 = 0
el2 = 0
together = 0
checkTrue = 0
checktogethertrue = 0
while True:
  for i in range(0, 100000):
    check = r.randint(1,6)
    el1 = r.randint(1,6)
    el2 = r.randint(1,6)
    if el1 == el2:
      together += 1
      if check == el1 and el2:
        checktogethertrue += 1
    elif check == el1 or check == el2:
      checkTrue += 1
  perSingleCheck = f.Fraction(checkTrue, 100000)    #100000-checkTrue
  perdoubleCheck = f.Fraction(checktogethertrue, checkTrue)   #perSingleCheck-checktogethertrue
  print("the percentage for single elephant " + str(perSingleCheck))
  print("\nthe percentage for double elephants " + str(perdoubleCheck))
  if input("\nre-run simulation? (y / n) ") == "n":
    break