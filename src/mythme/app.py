import tkinter as tk
from tkinter import ttk


def submit():
    name = name_entry.get().strip()
    option = combo.get()
    if not check_var.get():
        status_label.config(text="Please agree to the terms.", foreground="red")
        return
    if name:
        status_label.config(text=f"Hello, {name}! Option: {option}", foreground="green")
    else:
        status_label.config(text="Please enter your name.", foreground="red")


root = tk.Tk()
root.title("MythMe App")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding=16)
mainframe.grid(sticky="nsew")

ttk.Label(mainframe, text="MythMe App", font=("TkDefaultFont", 14, "bold")).grid(
    row=0, column=0, columnspan=2, pady=(0, 12)
)

ttk.Label(mainframe, text="Name:").grid(row=1, column=0, sticky="w", padx=(0, 8))
name_entry = ttk.Entry(mainframe, width=24)
name_entry.grid(row=1, column=1, pady=4)

ttk.Label(mainframe, text="Option:").grid(row=2, column=0, sticky="w", padx=(0, 8))
combo = ttk.Combobox(mainframe, values=["Option A", "Option B", "Option C"], state="readonly", width=22)
combo.current(0)
combo.grid(row=2, column=1, pady=4)

check_var = tk.BooleanVar()
ttk.Checkbutton(mainframe, text="Agree to terms", variable=check_var).grid(
    row=3, column=0, columnspan=2, pady=8, sticky="w"
)

ttk.Button(mainframe, text="Submit", command=submit).grid(
    row=4, column=0, columnspan=2, pady=(4, 8)
)

status_label = ttk.Label(mainframe, text="", foreground="green")
status_label.grid(row=5, column=0, columnspan=2)

ttk.Separator(mainframe, orient="horizontal").grid(
    row=6, column=0, columnspan=2, sticky="ew", pady=8
)

progress = ttk.Progressbar(mainframe, length=200, mode="determinate", value=0)
progress.grid(row=7, column=0, columnspan=2, pady=(0, 4))
progress_label = ttk.Label(mainframe, text="Progress: 0%")
progress_label.grid(row=8, column=0, columnspan=2)


def advance_progress():
    current = progress["value"]
    next_val = min(current + 20, 100)
    progress["value"] = next_val
    progress_label.config(text=f"Progress: {int(next_val)}%")
    if next_val < 100:
        root.after(500, advance_progress)


ttk.Button(mainframe, text="Start Progress", command=advance_progress).grid(
    row=9, column=0, columnspan=2, pady=(4, 0)
)

if __name__ == "__main__":
    root.mainloop()
