from tealight.net import connect, send
connect("chat.py")

send("hello!", echo = False)



def handle_message(message):
  print "Received message: " + message