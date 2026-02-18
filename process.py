import cv2
import subprocess
import os

def convert_to_svg(input_path, output_svg):
    img = cv2.imread(input_path)

    if img is None:
        raise Exception("Image not loaded")

    # Resize for better tracing
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    bmp_path = "outputs/bw.bmp"
    cv2.imwrite(bmp_path, thresh)

    subprocess.run(
        [
            "potrace",
            bmp_path,
            "-s",
            "-o",
            output_svg,
            "--turdsize",
            "5",
            "--alphamax",
            "1.0",
        ],
        check=True,
    )
