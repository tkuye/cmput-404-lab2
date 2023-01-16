import socket 
import multiprocessing as mp

def handle_connection(connection, address, max_packet_size, forward_address, forward_port):
    while True: 
        data = connection.recv(max_packet_size)
        if data:
            print('Data received:', data)
            new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            new_sock.connect((forward_address, forward_port))
            
            new_sock.send(data)
            response = new_sock.recv(max_packet_size)
            connection.sendall(response)
        else:
            print('No more data from', address)
            connection.close()
            break


def create_proxy_server(forward_address, forward_port, max_packet_size=32768):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.bind(('localhost', 8000))
    sock.listen(1)

    try:
        while True:
            connection, address = sock.accept()
            print('Connection from', address)
            process = mp.Process(target=handle_connection, args=(connection, address, max_packet_size, forward_address, forward_port))
            process.start() 
            

            

            
            
    except KeyboardInterrupt:
        print('Shutting down...')
        sock.close()

if __name__ == '__main__':
    create_proxy_server('www.google.com', 80)
