# -*- coding: utf-8 -*-
"""
演示多客户端请求grpc server

"""
import logging
import signal
import sys
import threading
import time
from concurrent import futures

from route_guide_client import run as runclient
from route_guide_server import serve


def main():
    logging.basicConfig()
    print("start grpc server:")
    server_thread = threading.Thread(target=serve, args=())

    server_thread.setDaemon(True)
    server_thread.start()
    # wait server start
    time.sleep(1)

    # start n clients

    n = 1
    client_executor = futures.ThreadPoolExecutor(n)

    client_executor.map(lambda i: runclient(), range(n))

    server_thread.join(3)
    print("exit")
    sys.exit(0)


if __name__ == '__main__':
    main()
