import socket

HOST = "127.0.0.1"
PORT = 8000

# Copied from https://realpython.com/python-sockets/

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"HELLO WORLD")
        data = s.recv(1024)

    print(f"Received {data!r}")


def main():
    print("client is running...")

    start_client()

if __name__ == "__main__":
    main()
