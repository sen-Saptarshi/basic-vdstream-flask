from flask import Flask, request, Response, send_from_directory, render_template
import os

app = Flask(__name__)

VIDEO_FOLDER = 'videos'

@app.route('/')
def index():
    videos = os.listdir(VIDEO_FOLDER)
    return render_template('index.html', videos=videos)

@app.route('/video/<filename>')
def video(filename):
    return render_template('video.html', filename=filename)

@app.route('/stream/<filename>')
def stream_video(filename):
    path = os.path.join(VIDEO_FOLDER, filename)
    range_header = request.headers.get('Range', None)
    if not range_header:
        return send_from_directory(VIDEO_FOLDER, filename)
    
    size = os.path.getsize(path)
    byte1, byte2 = 0, size - 1

    # Parse the Range header
    range_value = range_header.split('=')[1]
    if '-' in range_value:
        byte1, byte2 = range_value.split('-')
        byte1 = int(byte1) if byte1 else 0
        byte2 = int(byte2) if byte2 else size - 1

    byte1 = min(byte1, size - 1)
    byte2 = min(byte2, size - 1)
    length = byte2 - byte1 + 1

    with open(path, 'rb') as f:
        f.seek(byte1)
        data = f.read(length)

    rv = Response(data, 206, mimetype='video/mp4', content_type='video/mp4', direct_passthrough=True)
    rv.headers.add('Content-Range', f'bytes {byte1}-{byte2}/{size}')
    rv.headers.add('Accept-Ranges', 'bytes')
    return rv

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
