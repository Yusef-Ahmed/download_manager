import tkinter as tk
from tkinter import ttk, filedialog
from urllib.parse import urlparse
import requests
import threading
from tkinter import simpledialog

from FileHandle import handle_file_path

class DownloadManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Download Manager")
        self.progress_bars = []
        self.labels = []
        self.urls = []
        self.file_paths = []
        self.threads = []
        self.add_url_button = tk.Button(self.master, text="Add URL", command=self.add_url)
        self.add_url_button.pack(pady=5)
        self.start_button = tk.Button(self.master, text="Start Downloads", command=self.start_downloads)
        self.start_button.pack(pady=5)
        self.progress_frame = tk.Frame(self.master)
        self.progress_frame.pack(pady=10, fill=tk.BOTH, expand=True)


    def clearing(self):
        self.urls.clear()
        self.file_paths.clear()
        self.progress_bars.clear()
        self.labels.clear()
    def add_url(self):
        url = simpledialog.askstring("Enter URL", "Enter the download URL:")
        if url:
            self.urls.append(url)
            label = tk.Label(self.progress_frame, text=f"Preparing download for {urlparse(url).path.split('/')[-1]}")
            label.pack(pady=2)
            progress_bar = ttk.Progressbar(self.progress_frame, length=300, mode='determinate')
            progress_bar.pack(pady=2)
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
                            label.config(text=f"Downloading {file_path} ({downloaded}/{total} bytes)")
        except Exception as e:
            label.config(text=f"Error downloading {url}: {e}")

    def start_downloads(self):
        for i, url in enumerate(self.urls):
            file_path = handle_file_path(url)
            if not file_path:
                continue
            self.file_paths.append(file_path)

        for i, url in enumerate(self.urls):
            thread = threading.Thread(
                target=self.download,
                args=(url,self.file_paths[i], self.progress_bars[i], self.labels[i])
            )
            self.threads.append(thread)
            thread.start()
        self.clearing()
