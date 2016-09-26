#!/home/ubuntu/dev/cloud/bin/python2.7
import socket
import threading
from mpmath import mp

DIGITS = 100000


class ThreadedServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        print "Listening to clients."
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target=self.listen_to_client, args=(client, address)).start()

    def listen_to_client(self, client, address):
        while True:
            try:
                data = client.recv(1024)
                if data:
                    print "Got client request. Generating response."
                    response = self.calc_pie_digits()
                    client.send(response)
                    print "Sent a client: {}, pie's first {} digits.".format(address, DIGITS)
                    client.close()
                else:
                    raise socket.error('Client disconnected')
            except:
                client.close()
                return False

    def calc_pie_digits(self):
        mp.dps = DIGITS
        return str(mp.pi)

ThreadedServer('', 5678).listen()
