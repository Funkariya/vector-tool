from flask import Flask, render_template, request, send_file
import os
import uuid
from process import convert_to_svg

app = Flask(__name__)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():

    if "image" not in request.files:
        return "No file uploaded", 400

    img = request.files["image"]
    if img.filename == "":
        return "Empty file", 400

    # UI values
    colors = int(request.form.get("colors", 6))
    smooth = float(request.form.get("smooth", 1.0))
    bg = request.form.get("bg", "remove")

    uid = uuid.uuid4().hex
    input_path = f"{UPLOAD_DIR}/{uid}.png"
    output_svg = f"{OUTPUT_DIR}/{uid}.svg"

    img.save(input_path)

    convert_to_svg(
        input_path,
        output_svg,
        colors,
        smooth,
        bg == "remove"
    )

    return send_file(
        output_svg,
        as_attachment=True,
        download_name="vector.svg",
        mimetype="image/svg+xml"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
