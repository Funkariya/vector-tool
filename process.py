import cv2
import subprocess
import os
import numpy as np

def convert_to_svg(input_path, output_svg, colors=6, smooth=1.0, remove_bg=True):

    img = cv2.imread(input_path)
    if img is None:
        raise Exception("Image load failed")

    # Resize for quality
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Convert to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    Z = img_rgb.reshape((-1,3))
    Z = np.float32(Z)

    # KMeans color reduction
    K = max(2, min(colors, 12))
    _, labels, centers = cv2.kmeans(
        Z, K, None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
        10, cv2.KMEANS_RANDOM_CENTERS
    )

    centers = np.uint8(centers)
    reduced = centers[labels.flatten()].reshape(img_rgb.shape)

    # Convert reduced image to grayscale
    gray = cv2.cvtColor(reduced, cv2.COLOR_RGB2GRAY)

    # Adaptive threshold (NO hard black-white)
    bw = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    if remove_bg:
        bw = cv2.bitwise_not(bw)

    bmp_path = "outputs/input.bmp"
    cv2.imwrite(bmp_path, bw)

    # Potrace (SAFE flags only)
    subprocess.run([
        "potrace",
        bmp_path,
        "-s",
        "-o", output_svg,
        "--turdsize", "2",
        "--alphamax", str(smooth)
    ], check=True)
