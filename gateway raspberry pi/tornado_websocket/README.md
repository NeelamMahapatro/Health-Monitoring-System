#Transfer of data from Pi to Server over Websocket
* Install the library tornado-websocket in raspberry pi provided in this folder by follwing.
cd tornado-master
python / python3 setup.py install

* Run the mix.py code
 This python file accepts data from Base Raspberry pi and simultaneously send them to local server over Websocket.
## Make sure that the server code is running on the server side and in base raspberry pi, the client code is running. Provide the host and port accordingly. If there is any issue, that may be due to port.