import tkinter as tk
from tkinter import ttk
from app.utils import fetch

myth_config = fetch.mythtv_config()
dailyvid = fetch.dailyvid()


def play():
    vidspath = myth_config.storage_groups["Videos"][0]
    vidfile = f"{vidspath}/{dailyvid.video.file}"
    print(f"Playing video: {vidfile}")

    # name = name_entry.get().strip()
    # option = combo.get()
    # if not check_var.get():
    #     status_label.config(text="Please agree to the terms.", foreground="red")
    #     return
    # if name:
    #     status_label.config(text=f"Hello, {name}! Option: {option}", foreground="green")
    # else:
    #     status_label.config(text="Please enter your name.", foreground="red")


root = tk.Tk()
root.title("mythme")
root.geometry("600x200")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding=12)
mainframe.pack(expand=True, anchor="center")
# , sticky="nsew"
ttk.Label(mainframe, text="Daily Video", font=("TkDefaultFont", 14, "bold")).grid(
    row=0, column=0, columnspan=2, pady=(0, 12)
)

ttk.Label(mainframe, text=dailyvid.video.title, font=("TkDefaultFont", 12)).grid(
    row=1, column=0, columnspan=2, pady=(0, 8)
)
# name_entry = ttk.Entry(mainframe, width=24)
# name_entry.grid(row=1, column=1, pady=4)

# ttk.Label(mainframe, text="Option:").grid(row=2, column=0, sticky="w", padx=(0, 8))
# combo = ttk.Combobox(
#     mainframe, values=["Option A", "Option B", "Option C"], state="readonly", width=22
# )
# combo.current(0)
# combo.grid(row=2, column=1, pady=4)

# check_var = tk.BooleanVar()
# ttk.Checkbutton(mainframe, text="Agree to terms", variable=check_var).grid(
#     row=3, column=0, columnspan=2, pady=8, sticky="w"
# )

ttk.Button(mainframe, text="Play", command=play).grid(
    row=4, column=0, columnspan=2, pady=(4, 8)
)

progress = ttk.Progressbar(
    mainframe,
    length=500,
    mode="determinate",
    value=dailyvid.watched * 100 / dailyvid.total,
)
progress.grid(row=7, column=0, columnspan=2, pady=(10, 5))
progress_label = ttk.Label(
    mainframe, text=f"Watched {dailyvid.watched} of {dailyvid.total} videos"
)
progress_label.grid(row=8, column=0, columnspan=2)

if __name__ == "__main__":
    root.mainloop()
