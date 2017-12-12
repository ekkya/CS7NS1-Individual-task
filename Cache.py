import datetime
import os.path
import socket
import sys
from thread import *
from threading import Thread
import sqlite3

class client_thread(Thread):

    def __init__(self, addr, c):
        Thread.__init__(self)
        self.addr = addr
        self.c = c

    def run(self):
        while True:
            Cache

class Cache:
    def __init__(self):
        self.cache = {}
        self.max_cache_size = 50

    ##Add filename with timestamp to cache
    def setup(self, key, sock):
        input = sock.recv(2048)
        print input
        self.cache.update(input)
        sock.sendall(self.cache.encode())

    def update(self, conn, key, value):
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()

        self.cache[key] = {'date accessed': datetime.datetime.now(),
                           'value': value}

    def remove_oldest(self):
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_entry]['date_accessed']:
                oldest_entry = key
            self.cache.pop(oldest_entry)


def Main():
    host = 'localhost'
    port = 5014
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)
    print "Server Started"
    while True:
        c, addr = s.accept()
        print "Client Connected IP:" + str(addr)
        Thread = client_thread(addr, c)
        Thread.start()
        


if __name__ == '__main__':
    Main()
