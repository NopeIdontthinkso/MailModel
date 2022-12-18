import socket
import json
import constants

class Server():
    def __init__(self):
        self.bind_ip = constants.HOST
        self.bind_port = constants.PORT
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.bind_ip, self.bind_port))
        server.listen(constants.MAX_CLIENT_NUM)

def mailserverrun():
    #userdata
    user_dict = None
    with open('./user_dict.json', 'w') as f:
        s = f.read()
        user_dict = json.loads(s)
        print(user_dict)
    #build server
    server = Server()
    print(f"[*] Listening on {server.bind_ip}:{server.bind_port}")
    #talking to client
    while True:
        conn, addr = server.accept()
        login(conn)
        while True:
            data = conn.recv(1024).decode("utf-8").strip()
            print(f"Client send data: {data}")

            if data == "bye":
                conn.close()
                break

            conn.send("ACK!".encode())

def login(conn):
    conn.send(f"Log in...\naccount:".encode())
    data = conn.recv(1024).decode("utf-8").strip()
    # if data not in  


if __name__ == '__main__':
    mailserverrun()
