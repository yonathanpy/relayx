import socket
import threading

BUFFER = 8192

class Relay:
    def __init__(self, local_port, remote_host, remote_port):
        self.local_port = local_port
        self.remote_host = remote_host
        self.remote_port = remote_port

    def forward(self, src, dst):
        while True:
            try:
                data = src.recv(BUFFER)
                if not data:
                    break
                dst.sendall(data)
            except:
                break

    def handle(self, client):
        remote = socket.socket()
        remote.connect((self.remote_host, self.remote_port))

        t1 = threading.Thread(target=self.forward, args=(client, remote))
        t2 = threading.Thread(target=self.forward, args=(remote, client))

        t1.start()
        t2.start()

    def start(self):
        server = socket.socket()
        server.bind(("0.0.0.0", self.local_port))
        server.listen(50)

        print(f"[RELAY ACTIVE] {self.local_port} -> {self.remote_host}:{self.remote_port}")

        while True:
            client, addr = server.accept()
            print(f"[SESSION] {addr}")
            threading.Thread(target=self.handle, args=(client,)).start()


if __name__ == "__main__":
    r = Relay(9000, "example.com", 80)
    r.start()
