import random
import string 
from tornado.ioloop import IOLoop, PeriodicCallback 
from tornado import gen 
from tornado.websocket import websocket_connect 
import serial

ser = serial.Serial('/dev/ttyArduino', 115200, 8,'N', 1, timeout=5)
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

class Client(object):
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.connect()
        PeriodicCallback(self.keep_alive, 3000).start()
        self.ioloop.start()
    
    @gen.coroutine
    def connect(self):
        print("trying to connect")
        try:
            self.ws = yield websocket_connect(self.url)
            print(self.ws)
        except Exception:
            print("connection error")
            
        else:
            print("connected")
            self.run()
    
    @gen.coroutine
    def run(self):
        while True:
            msg = yield self.ws.read_message()
            print(msg)
            if msg is None:
                print("connection closed")


    def keep_alive(self):
        if self.ws is None:
            self.connect()
        else:
            print("Sent to server")
            data =ser.readline()
            self.ws.write_message(data)

if __name__ == "__main__":
    client = Client("ws://10.14.79.58:1023", 1)
