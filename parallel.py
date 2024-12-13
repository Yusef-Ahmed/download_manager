import requests # type: ignore
from tqdm import tqdm # type: ignore

def download_file(url, output_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))  # Total size in bytes

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

# Example usage
if __name__ == "__main__":
    download_url = input("Enter the direct download URL: ")
    output_file_path = input("Enter the output file path: ")
    download_file(download_url, output_file_path)