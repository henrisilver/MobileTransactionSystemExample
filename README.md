# MobileTransactionSystemExample
Modeling an example of a real-time transaction system that has a static server and mobile nodes connected to the server via wireless networks, introducing latency. The client, mobile nodes implement a "cache" of part of the data of the server, reducing the amount of communication needed. Based on the solution proposed by Narasayya: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.51.7796&amp;rep=rep1&amp;type=pdf

Instructions:
1- Run server
  $ python server.py
  
2- Run at least an instance of the client (more than an instance is needed to make data on the client outdated)
  $ python client.py
  
3- On the client, type 1 to make a transaction or 0 to quit

4- To quit the server, hit CTRL+C

Usage example:
Client 1 -> type 1
Client 1 -> type 1
Client 2 -> type 1
Client 2 -> type 1
Client 1 -> type 1
Cleint 1 -> type 0
Cleint 2 -> type 0
Server => CTRL+C to shutdown.
