from flask import Flask, render_template, request, send_file
import os
import uuid

app = Flask(__name__)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        if "image" not in request.files:
            return "NO FILE FOUND", 400

        file = request.files["image"]

        if file.filename == "":
            return "EMPTY FILE", 400

        filename = str(uuid.uuid4()) + ".png"
        path = os.path.join(UPLOAD_DIR, filename)

        file.save(path)

        # 🔥 TEST SUCCESS: return same image
        return send_file(path, as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
