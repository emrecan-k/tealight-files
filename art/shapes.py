from tealight.art import (color, rectangle, line, spot, circle, box, image, text, background)

color("blue")

spot(300,200,20)
circle(300,200,50)
box(250,250,100,100)
def handle_mousemove(x,y,button):
  global lastx, lasty
  
  if button == "left":
    
    ("blue")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
  