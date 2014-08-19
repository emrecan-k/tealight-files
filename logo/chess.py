from tealight.logo import move, turn
n=0
i = 0
size=30
def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
while i < 4:
  while n < 7:
    square(size)
    move(size)
    square(size)
    n = n + 1 
  n = 1
  turn(270)
  square(size)
  turn(-90)
  while n < 7:
    square(size)
    move(size)
    square(size)
    n = n + 1
  n = 1
  move(size)
  turn(90)
  move(size)
  square(size)
  turn(180)
  i=i+1