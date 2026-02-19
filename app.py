from flask import Flask, render_template, request, send_file
from process import convert_to_svg
import os
import uuid

app = Flask(__name__)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        if "image" not in request.files:
            return "No file", 400

        file = request.files["image"]
        if file.filename == "":
            return "Empty filename", 400

        uid = str(uuid.uuid4())
        input_path = f"{UPLOAD_DIR}/{uid}.png"
        output_svg = f"{OUTPUT_DIR}/{uid}.svg"

        file.save(input_path)

        colors = int(request.form.get("colors", 6))
        smooth = float(request.form.get("smooth", 1.0))
        remove_bg = request.form.get("bg") == "remove"

        convert_to_svg(input_path, output_svg, colors, smooth, remove_bg)

        return send_file(output_svg, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
