from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(1, edges):
    move(size)
    turn(angle)
    
polygon(6,150)