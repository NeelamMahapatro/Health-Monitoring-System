# Transfer of data from Pi to Server over Mqtt

##Make sure HiveMQ or any broker is installed in this raspberry pi

* Install the library paho-mqtt in raspberry pi provided in this folder by follwing.
cd paho.mqtt.python-master
python / python3 setup.py install

* Run the rpitoserver.py and server.py code.
  In rpitoserver code, base raspberry pi is publishing data and server has subscribed for those.

  In servertorpi code, server is publishing data and base raspberry pi has subscribed for those.


## Make sure about the host and port running in both the code.

