import cv2
import subprocess
import os
import uuid

def convert_to_svg(input_img, output_svg, colors, smooth, remove_bg):

    temp_bmp = f"/tmp/{uuid.uuid4().hex}.bmp"

    # Read image
    img = cv2.imread(input_img)
    if img is None:
        raise Exception("Image not readable")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binary threshold (best for logos)
    _, bw = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Save BMP for potrace
    cv2.imwrite(temp_bmp, bw)

    # Potrace command
    cmd = [
        "potrace",
        temp_bmp,
        "-s",
        "-o", output_svg,
        "--turdsize", "5",
        "--alphamax", str(smooth),
        "--opttolerance", "0.2"
    ]

    subprocess.run(cmd, check=True)

    # Cleanup
    if os.path.exists(temp_bmp):
        os.remove(temp_bmp)
