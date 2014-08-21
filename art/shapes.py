from tealight.art import (color, rectangle, line, spot, circle, box, image, text, background)

color("blue")

spot(300,200,20)
circle(300,200,50)
box(250,250,100,100)
def handle_mousedown(x,y,button):
  global lastx, lasty
  
  if button == "left" and 350 > x > 250 and 350 > y > 250:
    
    color("red")
    box(250, 250, 100, 100)
  