import socket
import time
import _thread

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("0.0.0.0", 8080))
s.listen(10)
http_response=b"""HTTP/1.1 200 OK\r
Content-Length: 10\r

hi there\n\r\n"""
# wait for connection
def response(conn):
    time.sleep(0.5)
    print(str(conn.recv(4096)))
    conn.send(http_response)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

while True:
    conn, address = s.accept()
    _thread.start_new_thread(response,(conn,))

s.close()
