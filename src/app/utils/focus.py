import subprocess  # nosec


def set_focus(window_title: str):
    subprocess.run(["/usr/bin/wmctrl", "-a", window_title], check=True)  # nosec
