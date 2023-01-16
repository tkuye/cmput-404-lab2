import socket


def connect_socket(proxy_host, target_host, target_port, max_packet_size=32768):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((target_host, target_port))
    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % proxy_host
    sock.send(request.encode())
    response = sock.recv(max_packet_size)
    sock.close()
    print(response.decode())


if __name__ == '__main__':
    connect_socket('www.google.com', 'localhost', 8000)