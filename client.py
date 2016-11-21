from dataModel import DataModel
import cPickle as pickle
import socket
import sys

data = DataModel(0,10)
option = 1

HOST, PORT = "localhost", 9999


while option != 0:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        option = int(input("Enter 1 to send transaction to server, 0 to quit: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    if option != 0:

        print "Local data before transaction: id = {}, data = {}".format(data.ident, data.data)
        data.transaction()
        print "Local data after transaction: id = {}, data = {}".format(data.ident, data.data)
        print "Sending..."
        
        try:

            # Create a socket (SOCK_STREAM means a TCP socket)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(pickle.dumps(data, -1))

            # Receive data from the server
            received = sock.recv(1024)

            if received == "Success":
                print "Transaction successful."
                # Update local id of data
                data.updateId(data.ident + 1)
            else:
                print "Transaction failed. Local copy outdated."
                processedData = pickle.loads(received)
                print "Received data: id = {}, data = {}".format(processedData.ident, processedData.data)
                data.updateDataAndId(processedData.data, processedData.ident)

        
        finally:
            sock.close()



