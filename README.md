# Flask Video Streaming Server 📺

![Demo Screenshot](static/thumbnail-placeholder.png)

A modern Flask-based video streaming platform with YouTube-style interface featuring hover previews, theme toggling, and dynamic video detection.

---

## Features ✨

- 🎥 Auto-detection of videos in `/videos` directory  
- 🖼️ Auto-generated preview thumbnails using FFmpeg  
- 🌗 Light/dark theme with local storage persistence  
- 📱 Fully responsive design (desktop & mobile)  
- ⚡ Hover-to-preview functionality  
- 🔍 Dynamic video scanning  

---

## Prerequisites

- Python 3.7+
- FFmpeg installed and in system PATH
- Basic terminal knowledge

---

## 🛠️ Installation & Setup

### 1. Clone and Prepare

```bash
git clone https://github.com/yourusername/flask-video-server.git
cd flask-video-server
```

### 2. Virtual Environment

```bash
# Create environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Required packages:
> - Flask==2.3.2  
> - Waitress==2.1.2  
> - Flask-CORS==3.0.10

---

## ⚙️ Configuration

1. Add your videos to the `videos/` folder  
   - Supported formats: MP4, MKV, AVI, MOV, etc.
2. (Optional) Customize the default thumbnail in `static/thumbnail-placeholder.png`

---

## 🚀 Launching the Server

### Development Mode

```bash
python video_server.py
```

### Production Mode

```bash
waitress-serve --port=5000 video_server:app
```

Access at: [http://localhost:5000](http://localhost:5000)

---

## 🧩 Customization Options

Enhance your server with:
```diff
+ User authentication system
+ Video upload functionality
+ Metadata management (titles, descriptions)
+ Custom UI themes
+ Playlist support
```

---

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Previews not generating | Verify FFmpeg installation |
| Slow first load | Allow time for thumbnail generation |
| Video playback issues | Check file permissions and codecs |
| Styling problems | Clear browser cache |

---

## 📜 Project Structure

```
flask-video-server/
├── videos/            # Video storage
├── static/            # Static files
│   ├── thumbnails/    # Auto-generated previews
│   └── styles/        # CSS files
├── templates/         # HTML templates
├── video_server.py    # Main application
└── requirements.txt   # Dependencies
```

---

## 📞 Contact

**Developer:** Samson Charles  
**Specialties:** Python Development · Cybersecurity · CTF  
**Contact:** [WhatsApp](https://wa.me/255710008454)

---

## 📄 License

**MIT License** — Free for modification and distribution

---

🎬 **Enjoy your self-hosted video platform!** 🍿  
