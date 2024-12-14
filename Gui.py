import tkinter as tk
from Download import DownloadManager


root = tk.Tk()
root.title("Parallel Downloader")
root.configure(background='#242424')

app = DownloadManager(root, 2)
root.mainloop()
