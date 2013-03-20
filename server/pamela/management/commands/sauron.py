import zmq, json
from pamela.views import update_macs
from django.core.management.base import BaseCommand
from optparse import make_option

class Command(BaseCommand):
    def handle(self, *args, **options):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://0.0.0.0:8000")

        while True:
            msg = socket.recv()
            print "Got", msg, "updating"
            try:
                update_macs(json.loads(msg))
                socket.send('200. OK')
            except:
                socket.send('500. Error')
                raise
