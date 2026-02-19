import cv2
import numpy as np
import subprocess
import os
from PIL import Image

def convert_to_svg(input_path, output_svg, colors=6, smooth=1.0, remove_bg=False):

    img = cv2.imread(input_path)
    if img is None:
        raise Exception("Image load failed")

    # Resize for better quality
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    if remove_bg:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
        img = cv2.bitwise_and(img, img, mask=mask)

    # Color reduction
    Z = img.reshape((-1,3))
    Z = np.float32(Z)

    K = colors
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    result = res.reshape((img.shape))

    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    bmp_path = output_svg.replace(".svg", ".bmp")
    cv2.imwrite(bmp_path, bw)

    subprocess.run([
        "potrace",
        bmp_path,
        "-s",
        "-o",
        output_svg,
        "--alphamax", str(smooth),
        "--turdsize", "5"
    ], check=True)

    os.remove(bmp_path)
