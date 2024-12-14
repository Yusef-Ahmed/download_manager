from tkinter import filedialog
import requests

def handle_file_name(url):
    try:
        path = requests.get(url, stream=True).headers.get(
                "Content-Disposition") or "filename='UnKnown.abc'"
        path = path.split("filename=")[-1][1:-1]
        extension = "." + path.split('.')[-1]
        path = path.encode('latin1').decode('utf-8')
        return path,extension
    except Exception as e:
        return None,None
    
def handle_file_path(url):
    path,extension = handle_file_name(url)
    if path:
        file_path = filedialog.asksaveasfilename(
            filetypes=[("All files", "*.*")],
            defaultextension=extension,
            initialfile=path)
        return file_path
    return None
    