# Flask Video Streaming App - VDSTREAM

A simple Flask application for streaming local video files with a dark-themed interface.

## Features

- Lists available video files.
- Streams videos without requiring full downloads.
- Clean and professional dark-themed UI.

## Directory Structure

```
/video-streaming-app
|-- app.py
|-- videos/
|-- templates/
|   |-- index.html
|   |-- video.html
|-- static/
    |-- css/
        |-- styles.css
```

## Setup and Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sen-Saptarshi/basic-vdstream-flask.git
   cd basic-vdstream-flask
   ```

2. **Install dependencies:**

   ```bash
   pip install Flask
   ```

3. **Add your video files to the `videos` directory.**

4. **Run the application:**

   ```bash
   python app.py
   ```

5. **Access the app in your browser:**

   Open `http://127.0.0.1:8080` (or your specified IP and port).
