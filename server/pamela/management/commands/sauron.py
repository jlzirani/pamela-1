import zmq, json
from pamela.views import update_macs
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5000")

while True:
    msg = socket.recv()
    print "Got", msg, "updating"
    try:
        update_macs(json.loads(msg))
        socket.send('200. OK')
    except:
        socket.send('500. Error')
        raise
