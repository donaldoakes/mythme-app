import tkinter as tk
from tkinter import ttk
from datetime import datetime
from app.utils import fetch

myth_config = fetch.mythtv_config()
dailyvid = fetch.dailyvid()

date_format = "%b %d, %Y"


root = tk.Tk()
root.title("mythme")
root.geometry("600x240")
root.resizable(False, False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

title = tk.StringVar()
action = tk.StringVar()
watched = tk.StringVar()
earliest = tk.StringVar()
latest = tk.StringVar()


def update_widgets(playable: bool):
    if playable:
        title.set(dailyvid.video.title)
        action.set("Play")
        progress["value"] = dailyvid.watched * 100 / dailyvid.total
        watched.set(f"Watched {dailyvid.watched} of {dailyvid.total} videos")
        earliest.set(f"Earliest: {dailyvid.earliest.strftime(date_format)}")
        latest.set(f"Latest: {dailyvid.latest.strftime(date_format)}")
    else:
        title.set("")
        action.set("Next")
        watched.set(f"Watched {dailyvid.watched + 1} of {dailyvid.total} videos")
        latest.set(f"Latest: {datetime.now().strftime(date_format)}")


def play():
    vidspath = myth_config.storage_groups["Videos"][0]
    vidfile = f"{vidspath}/{dailyvid.video.file}"
    print(f"Playing video: {vidfile}")
    update_widgets(False)


def next():
    title.set("Loading...")

    def after():
        global dailyvid
        dailyvid = fetch.dailyvid()
        update_widgets(True)

    root.after(100, after)


def do_action():
    if action_button["text"] == "Play":
        play()
    else:
        next()


mainframe = ttk.Frame(root, padding=(12, 6, 12, 16))
mainframe.grid(sticky="nsew")
mainframe.grid_rowconfigure(1, weight=1)
mainframe.grid_columnconfigure(1, weight=1)

ttk.Label(mainframe, text="Daily Video", font=("TkDefaultFont", 13, "bold")).grid(
    row=0, column=0, columnspan=2
)

ttk.Label(mainframe, textvariable=title, font=("TkDefaultFont", 12)).grid(
    row=1, column=0, columnspan=2
)

action_button = ttk.Button(mainframe, textvariable=action, command=do_action)
action_button.grid(row=2, column=0, columnspan=2, pady=(0, 8))

progress = ttk.Progressbar(mainframe, length=500, mode="determinate")
progress.grid(row=3, column=0, columnspan=2, pady=(20, 5))

ttk.Label(mainframe, textvariable=watched).grid(
    row=4, column=0, columnspan=2, pady=(0, 8)
)


ttk.Label(mainframe, textvariable=earliest).grid(
    row=5, column=0, padx=(40, 0), pady=(0, 8), sticky="w"
)
ttk.Label(mainframe, textvariable=latest).grid(
    row=5, column=1, padx=(0, 40), pady=(0, 8), stick="e"
)

update_widgets(True)


if __name__ == "__main__":
    root.mainloop()
