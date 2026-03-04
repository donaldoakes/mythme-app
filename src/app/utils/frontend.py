import socket
import time
from app.utils import focus
from app.utils.config import config

frontend_title = "MythTV Frontend"


def play_video(vidfile: str):
    host = config.mythfrontend.socket_host
    port = config.mythfrontend.socket_port
    test_mode = config.mythfrontend.test_mode

    if test_mode:
        print(f"Test mode play file: {vidfile}")
        time.sleep(5)
        return

    client_socket = socket.socket()
    client_socket.connect((host, port))

    client_socket.send(("jump mainmenu\n").encode("utf-8"))
    response_data = client_socket.recv(1024).decode()
    print(f"Jump response: '{response_data}'")
    time.sleep(1)
    client_socket.send((f"play file {vidfile}\n").encode("utf-8"))
    response_data = client_socket.recv(1024).decode()
    print(f"Play response: '{response_data}'")
    client_socket.send(b"exit")
    client_socket.close()

    focus.grab(frontend_title)
