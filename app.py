from flask import Flask, render_template, request, send_file
import os
from process import convert_to_svg

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if not file:
            return "No file uploaded", 400

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_svg = os.path.join(OUTPUT_FOLDER, "result.svg")

        file.save(input_path)

        # ✅ YAHI ADD KARNA THA
        colors = int(request.form.get("colors", 6))
        smooth = float(request.form.get("smooth", 1.0))
        remove_bg = request.form.get("bg") == "remove"

        convert_to_svg(input_path, output_svg, colors, smooth, remove_bg)

        return send_file(output_svg, as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
