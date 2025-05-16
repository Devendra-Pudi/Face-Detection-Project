
# Face Detection Project

This project implements real-time face detection using the YOLO (You Only Look Once) model, integrated with a Gradio interface for ease of use.

## Features

- Real-time face detection using YOLO.
- User-friendly interface powered by Gradio.
- Modular codebase with separate scripts for detection and application logic.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Devendra-Pudi/Face-Detection-Project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Face-Detection-Project
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using the following command:

```bash
python app.py
```

This will launch the Gradio interface in your default web browser, allowing you to upload images and perform face detection.

## Project Structure

- `app.py`: Main application script that launches the Gradio interface.
- `detect_faces.py`: Contains the logic for detecting faces using the YOLO model.
- `requirements.txt`: Lists all the Python dependencies required to run the project.

## License

This project is open-source and available under the [MIT License](LICENSE).
