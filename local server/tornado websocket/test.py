import logging 
import tornado.web 
import tornado.websocket 
import tornado.ioloop 
import tornado.options 
#import mysql.connector 
#from mysql.connector import Error
#from mysql.connector import errorcode
#from tornado.options import define, options

#define("1024", default=3000, help="run on the given port", type=int) 
class sen:
  def __init__(self, pbm, spo2, temp, airflow, body_pos, skin_cond, skin_resist, skin_volt):
    self.pbm = pbm
    self.spo2 = spo2
    self.temp = temp
    self.airflow = airflow
    self.body_pos = body_pos
    self.skin_cond = skin_cond
    self.skin_resist = skin_resist
    self.skin_volt = skin_volt

sensor = sen("","","","","","","","")




class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_orgin(self,origin):
        return True
   
    def open(self):
        print ("Connection established with webserver for live plot")
        ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=3), self.send_data)

        
    def on_close(self):
        print("Closed")

    def send_data(self):
        try:
            print("Sending data for live plot")
            point_data= {'pbm': sensor.pbm, 'spo2': sensor.spo2, 'temp': sensor.temp, 'airflow': sensor.airflow}
            self.write_message(json.dumps(point_data))
            ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=1), self.send_data)
        except:
            pass


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", MainHandler)]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings) 

class MainHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
   
    def open(self):
        print("")
        #logging.info("A client connected.")
    def on_close(self):
        print("")
        #logging.info("A client disconnected")
   
    def on_message(self, message):
        print("Data got:....... "+message)
        #logging.info("message: {}".format(message))
        if(message.find(":")!= -1):
            param, value = message.split(":")
            if(param == "pbm"):
                sensor.pbm = value
            elif(param == "spo2"):
                sensor.spo2 = value
            elif(param == "temp"):
                sensor.temp = value
            elif(param == "airflow"):
                sensor.airflow = value
                try:
                    application = web.Application([(r'/static/(.*)', web.StaticFileHandler, {'path': os.path.dirname(__file__)}),
                                 (r'/websocket', WebSocketHandler)])
                    application.listen(8080)#web page
                except:
                    print("problem in connecting for liveplot")
            elif(param == "body_pos"):
                sensor.body_pos = value
            elif(param == "skin_cond"):
                sensor.skin_cond = value
            elif(param == "skin_resist"):
                sensor.skin_resist = value
            elif(param == "skin_volt"):
                sensor.skin_volt = value
                


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(1024)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()



