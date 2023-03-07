import socket

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# print(color.BOLD + 'Hello, World!' + color.END)

def client_program():
    host = socket.gethostname()
    port = 2023

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'q':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Reply from server: {str(data)}")
        message = input(" -> ")
    client_socket.close()


if __name__ == '__main__':
    client_program()