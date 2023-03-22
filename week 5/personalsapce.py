import math as m
print("Welcome to the Social Situation Analyzer System")
print("\nPerson one")
person1 = input("  name: ")
pos1 = input("  position (x, y): ")
rad1 = int(input("  space radius: "))
pos1x, pos1y = map(int, pos1.split(', '))
pos1x, pos1y = ((pos1x,pos1y))

print("\nPerson two")
person2 = input("  name: ")
pos2 = input("  position (x,y): ")
rad2 = int(input("  space radius: "))
pos2x, pos2y = map(int, pos2.split(', '))
pos2x, pos2y = ((pos2x,pos2y))

def dis(p1x, p1y, p2x, p2y):
  return m.sqrt((p2x - p1x)**2  +  (p2y - p1y)**2)
distance = dis(pos1x, pos1y, pos2x, pos2y)

print(distance)
# over lap
if (rad1 + rad2) >= distance:
  print("Over laping radius")
  if rad1 > rad2:
    if distance < rad1:
      print(str(person2) + " is in " + str(person1) + "'s space")
  elif rad1 <= rad2:
    if distance < rad2:
      print(str(person1) + " is in " + str(person2) + "'s space")
else:
  print("they have enough room")