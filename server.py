import socket

HOST = "127.0.0.1"
PORT = 8000

# Copied from https://realpython.com/python-sockets/

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


def main():
    print("servere is running...")
    
    start_server()

if __name__ == "__main__":
    main()
