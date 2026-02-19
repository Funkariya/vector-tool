from flask import Flask, render_template, request, send_file
import os
from process import convert_to_svg

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
        return "No image uploaded", 400

    file = request.files["image"]
    if file.filename == "":
        return "Empty filename", 400

    # OPTIONS FROM UI
    colors = int(request.form.get("colors", 6))
    smooth = float(request.form.get("smooth", 1.0))
    bg = request.form.get("bg", "remove")

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_svg = os.path.join(OUTPUT_FOLDER, "result.svg")

    file.save(input_path)

    # ⚠️ SAFE CALL (no hang)
    convert_to_svg(
        input_path=input_path,
        output_svg=output_svg,
        colors=colors,
        smooth=smooth,
        remove_bg=(bg == "remove")
    )

    # 🔥 IMMEDIATE DOWNLOAD
    return send_file(
        output_svg,
        as_attachment=True,
        download_name="vector.svg",
        mimetype="image/svg+xml"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
