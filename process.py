import subprocess
import os

def convert_to_svg(input_path, output_svg, detail="medium", remove_bg=True):
    scans = {
        "low": "4",
        "medium": "8",
        "high": "12"
    }.get(detail, "8")

    command = [
        "inkscape",
        input_path,
        "--export-type=svg",
        f"--export-filename={output_svg}",
        "--trace-bitmap",
        "--trace-colors",
        f"--trace-scans={scans}",
        "--trace-smooth",
        "--trace-optimize",
        "--trace-stack"
    ]

    if remove_bg:
        command.append("--trace-remove-background")

    subprocess.run(command, check=True)
