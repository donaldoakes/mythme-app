import socket
from app.utils.config import config
from app.utils.focus import set_focus


def play_video(vidfile: str):
    host = config.mythfrontend.socket_host
    port = config.mythfrontend.socket_port
    test_mode = config.mythfrontend.test_mode

    if test_mode:
        print(f"TEST MODE: {vidfile}")
        return

    client_socket = socket.socket()
    client_socket.connect((host, port))

    client_socket.send((f"play file {vidfile}\n").encode("utf-8"))
    data = client_socket.recv(4096).decode()
    print("Response from the server: " + data)
    client_socket.send(b"exit")
    client_socket.close()

    set_focus("MythTV Frontend")
