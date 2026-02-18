import subprocess
import os

def convert_to_svg(
    input_path,
    output_svg,
    colors=8,
    smooth=1.0,
    remove_bg=True
):
    cmd = [
        "inkscape",
        input_path,
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
