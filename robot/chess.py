from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
i=0
while i<4:
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
  turn(-1)
  n=0
  while n<4:
    move()
    n+=1
  turn(-1)
  i+=1
n=0
while n < 32:
 move()
 n = n+1
turn(-1)
i=0
while i<4:
  n=0
  while n < 32:
    move()
    n = n+1
  turn(-1)
  n = 0
  while n < 4:
    move()
    n +=1
  turn(-1)
  n=0
  while n <32:
    move()
    n+=1
  turn(1)
  n=0
  while n<4:
    move()
    n+=1
  turn(1)
  i+=1
n=0
while n < 32:
 move()
 n = n+1