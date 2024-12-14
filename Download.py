import tkinter as tk
from tkinter import ttk
import requests
import threading
from tkinter import simpledialog, messagebox

from FileHandle import handle_file_path, handle_file_name


class DownloadManager:
    def __init__(self, master, limit_download):
        self.master = master
        self.limit_download = limit_download
        self.progress_bars = []
        self.labels = []
        self.urls = []
        self.file_paths = []
        self.threads = []

        self.add_url_button = tk.Button(
            self.master, text="Add URL", command=self.add_url)
        self.add_url_button.pack(pady=25, padx=100)

        self.start_button = tk.Button(
            self.master, text="Start Downloads", command=self.start_downloads)
        self.start_button.pack(side="bottom", pady=15)

        self.progress_frame = tk.Frame(self.master)
        self.progress_frame.config(background='#242424')
        self.progress_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    def clearing(self):
        self.urls.clear()
        self.file_paths.clear()
        self.progress_bars.clear()
        self.labels.clear()

    def add_url(self):
        if self.limit_download <= len(self.urls):
            messagebox.showwarning("Invalid Url", f"اخرك يبنى {self.limit_download} قلل شويه")
            return
        url = simpledialog.askstring("Enter URL", "\t\t\tEnter the download URL:\t\t\t\n")
        if url:
            file_name, _ = handle_file_name(url)
            if not file_name:
                messagebox.showwarning("Invalid Url", f"اللينك غلط ياعم انت \n {url} ")
                return

            self.urls.append(url)
            label = tk.Label(self.progress_frame, text=f"Preparing download for {file_name}")
            label.pack(pady=5)
            label.configure(background="#242424", fg="white")
            progress_bar = ttk.Progressbar(self.progress_frame, length=300, mode='determinate')
            progress_bar.pack(pady=10, padx=100)
            self.labels.append(label)
            self.progress_bars.append(progress_bar)

    def download(self, url, file_path, progress_bar, label):
        try:
            with requests.get(url, stream=True, timeout=30) as r:
                r.raise_for_status()
                total = int(r.headers.get('content-length', 0)) or None
                downloaded = 0
                progress_bar['maximum'] = total
                with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            progress_bar['value'] = downloaded
                            label.config(text=f"Downloading {file_path.split(
                                '/')[-1]}\n {int((downloaded/total)*100)}%")
                    label.config(text=f"{file_path.split('/')[-1]} downloaded successfully\n100%")
        except Exception as e:
            label.config(text=f"Error downloading {url}: {e}")

    def start_downloads(self):
        for i, url in enumerate(self.urls):
            file_path = handle_file_path(url)
            self.file_paths.append(file_path)
        for i, url in enumerate(self.urls):
            thread = threading.Thread(
                target=self.download,
                args=(url, self.file_paths[i],
                      self.progress_bars[i], self.labels[i])
            )
            self.threads.append(thread)
            thread.start()
        self.clearing()
