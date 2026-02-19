from flask import Flask, render_template, request, send_file
import os
from process import convert_to_svg
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():

    if "image" not in request.files:
        return "No file", 400

    file = request.files["image"]
    if file.filename == "":
        return "No filename", 400

    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(input_path)

    colors = int(request.form.get("colors", 6))
    smooth = float(request.form.get("smooth", 1.0))
    remove_bg = request.form.get("bg") == "remove"

    output_svg = os.path.join(OUTPUT_FOLDER, "result.svg")

    convert_to_svg(input_path, output_svg, colors, smooth, remove_bg)

    return send_file(output_svg, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
