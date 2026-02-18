import subprocess
import os

def convert_to_svg(input_path, output_svg):
    """
    Full color, smooth vectorization (Vector Magic style)
    """

    if not os.path.exists(input_path):
        raise Exception("Input image not found")

    subprocess.run(
        [
            "inkscape",
            input_path,
            "--export-type=svg",
            f"--export-filename={output_svg}",
            "--trace-bitmap",
            "--trace-colors",
            "--trace-scans=8",
            "--trace-smooth",
            "--trace-optimize",
            "--trace-stack",
            "--trace-remove-background"
        ],
        check=True
    )
