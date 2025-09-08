# 📌 Pinterest Feed Image Downloader

A simple Python automation tool that uses **Selenium** to download the first 100 images from your Pinterest home feed.

---

## ✅ Features

- Opens Chrome and asks for manual login.
- Automatically scrolls Pinterest feed until it collects 100 images.
- Downloads images in batch into a local folder.
- Simple, easy-to-use, no complex setup required.

---

## ⚡ How It Works

1. Opens Chrome browser and navigates to [https://www.pinterest.com](https://www.pinterest.com).
2. Waits for you to log in manually (60 seconds).
3. Automatically scrolls the feed and collects image URLs.
4. Downloads up to **100 images** into the folder `pinterest_images/`.

---

## 🚀 Prerequisites

- Python 3.x installed
- Google Chrome installed
- ChromeDriver installed and in your system PATH
    - Download ChromeDriver:  
      [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

---

## ✅ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Pinterest-Image-Auto-Downloader.git
    cd pinterest-image-downloader
    ```

2. Install required Python packages:
    ```bash
    pip install selenium beautifulsoup4 requests
    ```

---

## 🎯 How to Run

```bash
python simple_pinterest_downloader.py
