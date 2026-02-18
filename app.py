@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        detail = request.form.get("detail", "medium")
        remove_bg = "remove_bg" in request.form

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_svg = os.path.join(OUTPUT_FOLDER, "result.svg")

        file.save(input_path)
        convert_to_svg(input_path, output_svg, detail, remove_bg)

        return send_file(output_svg, as_attachment=True)

    return render_template("index.html")
