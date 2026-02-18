import cv2
import subprocess
import os

def convert_to_svg(input_path, output_svg):
    img = cv2.imread(input_path)

    if img is None:
        raise Exception("Image not loaded")

    # upscale for better tracing
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 9, 75, 75)

    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    bw_path = "outputs/bw.png"
    cv2.imwrite(bw_path, thresh)

    subprocess.run(
        [
            "potrace",
            bw_path,
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

