from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, size, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + (size * cos(angle))
    y0 = y + (size * sin(angle))
    
    line(x, y, 2x, 2y)
    
    angle = angle + (2 * pi / spines)

star(300, 300, "blue", 100, 2000)
star(600, 400, "purple", 200, 2000)
star(450, 200, "orange", 125, 3000)