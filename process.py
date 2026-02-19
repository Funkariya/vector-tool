import subprocess
import os
import shutil

def convert_to_svg(input_img, output_svg, colors, smooth, remove_bg):
    """
    input_img  : uploaded raster image path
    output_svg : final svg output path
    colors     : number of colors (2,4,6,8)
    smooth     : edge smoothness (0.5 – 2.0)
    remove_bg  : True / False
    """

    # Safety check
    if not os.path.exists(input_img):
        raise FileNotFoundError("Input image not found")

    # Potrace works best on PGM/PPM → future ready
    # For now direct PNG works (basic)

    cmd = [
        "potrace",
        input_img,
        "-s",                 # SVG output
        "-o", output_svg,
        "--turdsize", "2",    # remove small noise
        "--alphamax", str(smooth),  # EDGE smoothness
        "--opttolerance", "0.4"
    ]

    # NOTE:
    # Potrace does NOT truly support "colors"
    # Colors handling = Phase-3 (quantization before trace)

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("Vector conversion failed") from e
