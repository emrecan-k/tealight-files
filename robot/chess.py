from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
n=0
while n < 32:
  move()
  n = n+1
turn(1)
n = 0
while n < 4:
  move()
  n +=1
turn(1)
n=0
while n <32:
  move()
  n+=1