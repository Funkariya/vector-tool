import subprocess
import os
import uuid

def convert_to_svg(input_path, output_svg, colors=6, smooth=1.0, remove_bg=True):
    tmp_svg = f"outputs/tmp_{uuid.uuid4().hex}.svg"

    cmd = [
        "inkscape",
        input_path,
        "--export-type=svg",
        f"--export-filename={tmp_svg}",
        "--trace-bitmap",
        "--trace-smooth",
        "--trace-optimize",
        f"--trace-colors={colors}",
        f"--trace-smooth-threshold={smooth}",
    ]

    if remove_bg:
        cmd.append("--trace-remove-background")

    # ⏱️ TIMEOUT = no infinite loading
    subprocess.run(cmd, check=True, timeout=25)

    os.replace(tmp_svg, output_svg)
