import os
from flask import Flask, send_file, render_template, send_from_directory, request
from waitress import serve

app = Flask(__name__, static_folder='static')

# Configuration
VIDEO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'videos')
HOST = "0.0.0.0"
PORT = 5000

# Create necessary directories
os.makedirs(VIDEO_DIR, exist_ok=True)

def get_video_entries(path, relative_path=""):
    """Get all video files and directories with navigation support"""
    entries = []
    current_path = os.path.join(path, relative_path) if relative_path else path
    
    # Add navigation buttons if not in root
    if relative_path:
        parent_path = os.path.dirname(relative_path)
        entries.append({
            'name': '← Home',
            'path': '',
            'is_home': True,
            'thumbnail': '/static/img/home-icon.png'
        })
        
        if parent_path:
            entries.append({
                'name': '↑ Up',
                'path': parent_path,
                'is_up': True,
                'thumbnail': '/static/img/up-icon.png'
            })

    try:
        for item in sorted(os.listdir(current_path)):
            item_path = os.path.join(current_path, item)
            rel_path = os.path.join(relative_path, item) if relative_path else item
            
            if os.path.isdir(item_path):
                entries.append({
                    'name': item,
                    'path': rel_path,
                    'is_folder': True,
                    'thumbnail': '/static/img/folder-icon.png'
                })
            
            elif os.path.isfile(item_path) and item.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.webm')):
                entries.append({
                    'name': os.path.splitext(item)[0],
                    'filename': rel_path,
                    'thumbnail': '/static/img/thumbnail-placeholder.png'
                })
    except Exception as e:
        print(f"Error reading directory: {str(e)}")
    
    return entries

@app.route('/')
def index():
    path = request.args.get('path', '')
    video_entries = get_video_entries(VIDEO_DIR, path)
    return render_template('index.html', 
                         videos=video_entries,
                         current_path=path)

@app.route('/stream/<path:filename>')
def stream_video(filename):
    video_path = os.path.join(VIDEO_DIR, filename)
    
    if not os.path.exists(video_path):
        return "File not found", 404
    
    current_path = os.path.dirname(filename)
    return render_template('player.html',
                         video_name=os.path.basename(filename),
                         video_url=f"/stream_file/{filename}",
                         current_path=current_path)

@app.route('/stream_file/<path:filename>')
def stream_file(filename):
    video_path = os.path.join(VIDEO_DIR, filename)
    return send_file(video_path, mimetype='video/mp4', conditional=True)

if __name__ == '__main__':
    print(f"Server running on http://{HOST}:{PORT}")
    print(f"Serving videos from: {VIDEO_DIR}")
    serve(app, host=HOST, port=PORT)
