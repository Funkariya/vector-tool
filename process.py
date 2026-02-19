import subprocess
import os

def convert_to_svg(input_img, output_svg, colors, smooth, remove_bg):

    cmd = [
        "inkscape",
        input_img,
        "--export-type=svg",
        f"--export-filename={output_svg}",
        "--trace-bitmap",
        f"--trace-colors={colors}",
        f"--trace-smooth={smooth}",
        "--trace-optimize"
    ]

    if remove_bg:
        cmd.append("--trace-remove-background")

    subprocess.run(cmd, check=True)
