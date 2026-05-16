<div align="center">

# 👤 Face Detection Project
### Real-time face detection using YOLO + Gradio

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![YOLO](https://img.shields.io/badge/YOLO-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)](https://ultralytics.com)
[![Gradio](https://img.shields.io/badge/Gradio-FF7C00?style=for-the-badge)](https://gradio.app)
[![Stars](https://img.shields.io/github/stars/Devendra-Pudi/Face-Detection-Project?style=for-the-badge)](https://github.com/Devendra-Pudi/Face-Detection-Project/stargazers)

> *Upload an image. Detect faces instantly with state-of-the-art YOLO — no setup friction.*

</div>

---

## 📖 Overview

**Face Detection Project** is a computer vision application that performs real-time face detection using the **YOLO (You Only Look Once)** deep learning model. The project is wrapped in a **Gradio** web interface, making it easy to upload images and visualize detection results without any frontend coding.

---

## ✨ Features

- 🚀 **YOLO-based detection** — fast and highly accurate face localization
- 🖼️ **Gradio UI** — upload images directly from the browser, no CLI needed
- 🧩 **Modular design** — clean separation between detection logic and application layer
- 📦 **Easy to extend** — swap the YOLO model or add video stream support
- 🔧 **Simple installation** — one requirements file, three steps to run

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python |
| Detection Model | YOLO (Ultralytics) |
| Computer Vision | OpenCV |
| UI Framework | Gradio |
| Hardware Support | CPU & GPU (auto-detect) |

---

## 🚀 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/Devendra-Pudi/Face-Detection-Project.git
cd Face-Detection-Project

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The Gradio interface will launch automatically in your default browser.

---

## 📁 Project Structure

```
Face-Detection-Project/
├── app.py              # Gradio app — launches the web interface
├── detect_faces.py     # Core YOLO face detection logic
└── requirements.txt    # Python dependencies
```

---

## 🧪 How It Works

1. User uploads an image via the Gradio interface
2. `detect_faces.py` runs YOLO inference on the image
3. Bounding boxes are drawn around detected faces
4. The annotated image is returned to the UI in real-time

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

Built with 👁️ by [Devendra Prasad Pudi](https://github.com/Devendra-Pudi)

⭐ Star this repo if you found it useful!

</div>
