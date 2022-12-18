import socket

bind_ip = "127.0.0.1"
bind_port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print(f"[*] Listening on {bind_ip}:{bind_port}")

def mailserverrun():

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
    while True:
        conn.send("Log in?(Y/N)".encode())
        data = conn.recv(1024).decode("utf-8").strip()
        if data == 'Y':
            break
        elif data == 'N':
            conn.send("so why the fuck do you open this".encode())
        else:
            conn.send("cannot read your shit".encode())

if __name__ == '__main__':
    mailserverrun()
