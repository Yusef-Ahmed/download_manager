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
  pip install tkinter requests
  ```

---

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd parallel-downloader
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
5. Monitor progress using the displayed progress bars and labels.

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



### Activity Diagram



---


## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the project.

---

## Acknowledgments

- **Tkinter**: For providing the GUI framework.
- **Requests**: For handling HTTP requests.
