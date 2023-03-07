
'''
Use the socket to write a simple web server running on your Raspberry Pi. 
When your server receives a request it should print “Got a request!” to the screen of the Raspberry Pi. 
Turn in your code and turn in a screen shot of your Raspberry Pi screen with “Got a request!” 
printed in order to demonstrate that it worked. 
In order to get the screen shot, you will need to set up your Raspberry Pi, 
run the server, and type the IP address of your Raspberry Pi into the address 
line of a web browser running on a desktop or a laptop. 
'''

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

def server_program():
    host = socket.gethostname()
    port = 2023
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(3)
    conn, address = server_socket.accept()
    print(f"\n{color.BOLD + color.UNDERLINE + color.RED}Got a request!{color.END}\n")
    print(f"...from {str(address)}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"from connected client: {str(data)}")
        #data = input(' -> ')
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    server_program()