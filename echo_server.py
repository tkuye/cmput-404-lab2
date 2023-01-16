import socket
import multiprocessing as mp 


def handle_connection(connection, address):
    while True:
        data = connection.recv(1024)
        if data:
            print('Data received:', data)
            connection.sendall(data)
        else:
            print('No more data from', address)
            connection.close()
            break

def create_echo_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.bind(('localhost', 8000))
    sock.listen(1)
    try:
        while True:
            connection, address = sock.accept()
            print('Connection from', address)
            process = mp.Process(target=handle_connection, args=(connection, address))
            process.start()
            
    except KeyboardInterrupt:
        print('Shutting down...')
        sock.close()

if __name__ == '__main__':
    create_echo_server()