import logging
import tornado.web
import tornado.websocket 
import tornado.ioloop 
import tornado.options 
import time

from tornado.options import define, options
from tornado.ioloop import IOLoop,PeriodicCallback
from tornado import gen 
from tornado.websocket import websocket_connect

class data:
    def __init__(self, incoming):
        self.incoming = incoming

obj = data("")
define("7000", default=3000, help="run on the given port", type=int)
class Client(object):
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.connect()
        #PeriodicCallback(self.keep_alive, 3000).start()
        self.ioloop.start()

    @gen.coroutine
    def connect(self):
        print("trying to connect")
        try:
            self.ws = yield websocket_connect(self.url)
        except Exception:
            print("Connection error")
        else:
            print("Connected")
            self.run()

    @gen.coroutine
    def run(self):
        while True:
            if self.ws is None:
                self.connect()
            else:
                print("Sent to server") 
                self.ws.write_message(obj.incoming) 
                time.sleep(2)
                self.ws = None 
                break


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", MainHandler)]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    
    def open(  self):
        print(" ")
        #logging.info("A client connected.")
    
    def on_close(self):
        print(" ")
        #logging.info("A client disconnected")
    
    def on_message(self, message):
        obj.incoming = message
        print("Got Message: "+message)
        try:
            client = Client("ws://10.14.96.52:8000",1)
            #print(message+":   and sent to server")
            #logging.info("message: {}".format(message)) 
        except:
            file = open('testfile.txt', 'a') 
            file.write(message+"\n")
            file.close()
            #print("Saved to file")

def main(): 
    tornado.options.parse_command_line() 
    app = Application()
    app.listen(7000)   #from base pi data wiill come in this port 8000
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
 
