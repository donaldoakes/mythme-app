import tkinter as tk
from tkinter import ttk
from app.utils import fetch

myth_config = fetch.mythtv_config()
dailyvid = fetch.dailyvid()

date_format = "%b %d, %Y"


def play():
    vidspath = myth_config.storage_groups["Videos"][0]
    vidfile = f"{vidspath}/{dailyvid.video.file}"
    print(f"Playing video: {vidfile}")


root = tk.Tk()
root.title("mythme")
root.geometry("600x240")
root.resizable(False, False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding=(12, 6, 12, 16))
mainframe.grid(sticky="nsew")
mainframe.grid_rowconfigure(1, weight=1)
mainframe.grid_columnconfigure(1, weight=1)

ttk.Label(mainframe, text="Daily Video", font=("TkDefaultFont", 13, "bold")).grid(
    row=0, column=0, columnspan=2
)

ttk.Label(mainframe, text=dailyvid.video.title, font=("TkDefaultFont", 12)).grid(
    row=1, column=0, columnspan=2
)

ttk.Button(mainframe, text="Play", command=play).grid(
    row=2, column=0, columnspan=2, pady=(0, 8)
)

progress = ttk.Progressbar(
    mainframe,
    length=500,
    mode="determinate",
    value=dailyvid.watched * 100 / dailyvid.total,
)
progress.grid(row=3, column=0, columnspan=2, pady=(20, 5))

ttk.Label(
    mainframe, text=f"Watched {dailyvid.watched} of {dailyvid.total} videos"
).grid(row=4, column=0, columnspan=2, pady=(0, 8))


ttk.Label(mainframe, text=f"Earliest: {dailyvid.earliest.strftime(date_format)}").grid(
    row=5, column=0, padx=(40, 0), pady=(0, 8), sticky="w"
)
ttk.Label(mainframe, text=f"Latest: {dailyvid.latest.strftime(date_format)}").grid(
    row=5, column=1, padx=(0, 40), pady=(0, 8), stick="e"
)

if __name__ == "__main__":
    root.mainloop()
