==================================================
           Flask Video Streaming Server
==================================================

This is a complete Flask-based video streaming server with a modern, YouTube-like interface. It includes dynamic previews using FFmpeg, light/dark themes, and clean styling.



Dependencies:
- flask==2.3.2
- waitress==2.1.2
- flask-cors==3.0.10

Also make sure `ffmpeg` is installed and available in your system path.

--------------------------------------------------
▶️ How to Run
--------------------------------------------------

1. Place your video files inside the `videos/` folder.

2. Start the server:

    python video_server.py

Or run using Waitress for production:

    waitress-serve --host=0.0.0.0 --port=5000 video_server:app

3. Open your browser and go to:

    http://localhost:5000

--------------------------------------------------
🎞 Features
--------------------------------------------------

- Auto-detects video files (mp4, mkv, avi, etc.)
- Auto-generates short previews using ffmpeg
- Clean grid UI with responsive design
- Video cards with hover preview
- Theme toggle (light/dark) with persistence
- Compatible with mobile and desktop


--------------------------------------------------
📁 Notes
--------------------------------------------------

- Preview generation may take a few seconds on first load.
- You can replace the `thumbnail-placeholder.png` image with custom thumbnails.
- The UI uses Font Awesome for icons.

--------------------------------------------------
🧠 Author's Note
--------------------------------------------------

This project was built to demonstrate modern Flask applications with frontend interactivity, media previewing, and full-stack integration.

Feel free to customize it, add authentication, or extend it with upload features or metadata!

--------------------------------------------------
👨‍💻 Contact
--------------------------------------------------

Developer: Samson Charles  
CTF Player | Python Dev | Ethical Hacker  
WhatsApp: https://wa.me/255710008454

--------------------------------------------------
📦 Requirements
--------------------------------------------------

Install required Python packages with:


   ## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flask-video-server.git
cd flask-video-server
pip install -r requirements.txt
