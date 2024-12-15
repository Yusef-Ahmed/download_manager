# File Downloader

## Overview

This project is a Python-based parallel downloader application built using the Tkinter library for the GUI. It allows users to:

- Add multiple download URLs.
- Download files concurrently using **multithreading**.
- Track progress via a dynamic GUI.

The application enforces a limit on the number of concurrent downloads and validates URLs before downloading.

---

## Features

- **User-Friendly Interface**: Simple and intuitive GUI for adding URLs and tracking downloads.
- **Multithreading**: Downloads multiple files concurrently to improve efficiency.
- **Dynamic Progress Tracking**: Real-time progress updates for each download.
- **File Validation**: Ensures that URLs and file paths are valid before starting the download.

---

## Prerequisites

Ensure the following are installed:

- Python 3.7 or higher
- Required Python libraries:
  ```bash
  pip install requests
  ```

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Yusef-Ahmed/download_manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd download_manager
   ```

3. Run the application:

   ```bash
   python Gui.py
   ```

---

## How to Use

1. Launch the application.
2. Click **Add URL** to input a download URL.
3. (Optional) Add more URLs as needed.
4. Click **Start Downloads** to begin downloading all added URLs.
5. Write file/s name/s (tip: specify the needed extension e.g. .mp3 for audio or .mp4 for video).
6. Monitor progress using the displayed progress bars and labels.

---

## Project Structure

```
parallel-downloader/
├── GUI.py             # Main entry point for the application
├── FileHandle.py      # Utility functions for file handling and validation
├── Download.py        # Core logic for managing downloads
└── README.md          # Project documentation
```

---

## Diagrams

### Sequence Diagram

![SequenceDiagram(2)](https://github.com/user-attachments/assets/0713b984-7b99-42d8-a08d-eda349b3a16b)


### Activity Diagram

![WhatsApp Image 2024-12-15 at 12 51 20](https://github.com/user-attachments/assets/3e4e2096-d0a8-4804-9298-6b99ea37601d)

----------------------------------------------------------------------------------------------------
![WhatsApp Image 2024-12-15 at 12 55 11](https://github.com/user-attachments/assets/31565e62-2aaf-4123-a70a-17d08971dea7)



---


## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the project.

---

## Acknowledgments

- **Tkinter**: For providing the GUI framework.
- **Requests**: For handling HTTP requests.
