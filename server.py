from dataModel import DataModel
import cPickle as pickle
import SocketServer
from random import randint
import threading
import time

data = DataModel(0,10)

class MyRequestHandlerWithStreamRequestHandler(SocketServer.StreamRequestHandler):
 
    def handle(self):
        time.sleep(randint(0,10))
        self.received = pickle.loads(self.request.recv(1024).strip())
        print "{}:{} sent id = {}, data = {}".format(self.client_address[0], self.client_address[1], self.received.ident, self.received.data)
        
        if data.ident > self.received.ident:
            print "The client has outdated data. Sending the following updated data: "
            print "Sending id = {}, data = {}".format(data.ident, data.data)
            self.request.sendall(pickle.dumps(data, -1))
        else:
            print "Updating content."
            data.updateData(self.received.data)
            self.request.sendall("Success") 
 
if __name__ == "__main__":
    print "Initializing server..."
    tcp_server = SocketServer.ThreadingTCPServer(("localhost", 9999), RequestHandlerClass=MyRequestHandlerWithStreamRequestHandler, bind_and_activate=False)
     
    tcp_server.allow_reuse_address = True
    tcp_server.server_bind()
    tcp_server.server_activate()
     
    tcp_server.serve_forever()