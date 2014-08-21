from tealight.net import connect, send
connect("chat.py")

send("hello!", echo = false)



def handle_message(message):
  print "Received message: " + message