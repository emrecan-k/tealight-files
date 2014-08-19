from tealight.logo import move, turn
n=0
def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
while n < 7:
  square(30)
  move(30)
  square(30)
  n = n + 1 