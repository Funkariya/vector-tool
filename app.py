from flask import Flask, render_template, request, send_file
import os, uuid
from process import convert_to_svg

app = Flask(__name__)

UPLOAD = "uploads"
OUTPUT = "outputs"
os.makedirs(UPLOAD, exist_ok=True)
os.makedirs(OUTPUT, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    img = request.files["image"]
    colors = int(request.form.get("colors", 6))
    smooth = float(request.form.get("smooth", 1.0))
    remove_bg = request.form.get("bg") == "remove"

    uid = str(uuid.uuid4())
    input_path = f"{UPLOAD}/{uid}.png"
    output_path = f"{OUTPUT}/{uid}.svg"

    img.save(input_path)

    convert_to_svg(input_path, output_path, colors, smooth, remove_bg)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
