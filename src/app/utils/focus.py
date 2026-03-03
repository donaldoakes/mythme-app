import subprocess  # nosec


def grab(window_title: str):
    subprocess.run(["/usr/bin/wmctrl", "-a", window_title], check=True)  # nosec
