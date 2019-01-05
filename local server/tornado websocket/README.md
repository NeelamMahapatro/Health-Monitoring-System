#Transfer of data from Pi to Server over Websocket
* Install the library tornado-websocket in raspberry pi provided in this folder by follwing.
cd tornado-master
python / python3 setup.py install

* Run the py_server.py code
 This python file accepts data from Gateway Raspberry pi or Base Raspberry pi depending on the host and port
## Make sure that the port is correct. Before running any client code, run this server file