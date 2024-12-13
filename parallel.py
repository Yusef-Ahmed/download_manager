import requests
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog
from urllib.parse import urlparse


def download_file(url, output_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get(
        'content-length', 0))

    with open(output_path, 'wb') as file, tqdm(
        desc="Downloading",
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as progress_bar:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            progress_bar.update(len(data))


def handle_file_path(url):
    path = requests.get(url, stream=True).headers.get(
        "Content-Disposition") or "filename='UnKnown.xxx'"
    path = path.split("filename=")[-1][1:-1]
    extension = "." + path.split('.')[-1]
    path = path.encode('latin1').decode('utf-8')
    
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', 1)

    root.update()
    file_path = filedialog.asksaveasfilename(
        filetypes=[("All files", "*.*")],
        defaultextension=extension,
        initialfile=path)
    return file_path


if __name__ == "__main__":
    download_url = input("Enter the URL: ")
    file_path = handle_file_path(download_url)
    if file_path:
        download_file(download_url, file_path)
    else:
        print("Download canceled")
