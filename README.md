# Image → Vector Converter (SVG)

A clean, fast, and open-source **Image to SVG Vector Converter**  
Built with **Flask + Potrace + ImageMagick**

🔗 Live Demo: https://vector-tool.onrender.com

---

## ✨ Features

- Convert **PNG / JPG → True SVG Paths**
- No raster images inside SVG
- Infinite zoom (print-ready)
- Perfect for:
  - Logos
  - T-shirts
  - Stickers
  - CNC / Laser
  - Vinyl cutting

---

## ⚙️ Tech Stack

- Python (Flask)
- Potrace (vector tracing)
- ImageMagick (bitmap processing)
- Docker
- Render Deployment

---

## 🚀 How It Works

1. Upload image
2. Image converted to black & white bitmap
3. Potrace traces bitmap into **real SVG paths**
4. SVG downloaded instantly

---

## 🖥 Run Locally

```bash
git clone https://github.com/Funkariya/vector-tool.git
cd vector-tool
docker build -t vector-tool .
docker run -p 10000:10000 vector-tool
