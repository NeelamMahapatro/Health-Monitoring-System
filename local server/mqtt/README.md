# Transfer of data from Pi to Server over Mqtt

## Make sure HiveMQ or any broker is installed in this server

* Install the library paho-mqtt in server provided in this folder by follwing.
cd paho.mqtt.python-master
python / python3 setup.py install

* client.py:
	subscribes for a particular topic to the local broker and whenever a client sends a message, it recieves those data with the same topic.

* oximeter.py:
	Accepts the data coming from oximeter which is connected serially to the base raspberry pi by subscribing with "oximeter" topic and insert them to database.

* signup.py:
    Accepts signup and signin information form the GUI of base raspberry pi and take necessary action by inserting or selecting from the database.


## Make sure about the host and port running in every code.

