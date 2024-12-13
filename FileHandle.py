from tkinter import filedialog
import requests

def handle_file_path(url):
    path = requests.get(url, stream=True).headers.get(
        "Content-Disposition") or "filename='UnKnown.xxx'"
    path = path.split("filename=")[-1][1:-1]
    extension = "." + path.split('.')[-1]
    path = path.encode('latin1').decode('utf-8')

    file_path = filedialog.asksaveasfilename(
        filetypes=[("All files", "*.*")],
        defaultextension=extension,
        initialfile=path)
    return file_path