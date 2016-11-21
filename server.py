from dataModel import DataModel
import cPickle as pickle
import SocketServer

data = DataModel(0,10)

class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        
        self.received = pickle.loads(self.request.recv(1024).strip())
        print "{} sent id = {}, data = {}".format(self.client_address[0], self.received.ident, self.received.data)
        
        if data.ident > self.received.ident:
            print "The client has outdated data. Sending the following updated data: "
            print "Sending id = {}, data = {}".format(data.ident, data.data)
            self.request.sendall(pickle.dumps(data, -1))
        else:
            print "Updating content."
            data.updateData(self.received.data)
            self.request.sendall("Success")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    print "Initializing server..."

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()