from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
for i in range(0, 500):
  move()
  touch()
  if touch() == None:
    turn(-1)
     